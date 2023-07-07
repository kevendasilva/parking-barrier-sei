from dotenv import load_dotenv
import logging
import os
import RPi.GPIO as GPIO
import time

from auth.token import get_token
from datetime import datetime, timedelta
from setup import *

from request.get import get
from request.post import post

from barrier.actuator import Actuator
from barrier.barrier import Barrier
from barrier.led import Led
from barrier.presence_sensor import PresenceSensor
from barrier.utils.load_configs import load_configs

from plate_identifier_model import detect_plate

load_dotenv()


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    handlers=[
        logging.FileHandler('log', mode='a'),
        logging.StreamHandler()
    ]
)


def setup():
    configs = load_configs(root_dir = os.getcwd())

    logging.info("Configurando atuadores e sensores...")

    logging.info("Iniciando atuador.")
    actuator = Actuator(*configs["actuator"]["pins"])
    time.sleep(0.5)

    logging.info("Iniciando LEDs de sinalização.")
    warning_led = Led(pin = configs["leds"]["warning"])
    success_led = Led(pin = configs["leds"]["success"])
    logging.info("Iniciando o sensor de presença.")
    presence_sensor = PresenceSensor(trigger_pin = configs["presence_sensor"]["trigger_pin"], echo_pin = configs["presence_sensor"]["echo_pin"])

    logging.info("Iniciando a cancela.")
    barrier = Barrier(actuator, warning_led, success_led, presence_sensor)

    logging.info("Configuração finalizada.")

    return barrier

def loop(barrier):
    logging.info("Começo do loop da aplicação.")

    while True:
        if (barrier.vehicle_is_near()):
            logging.info("Carro está próximo.")

            plate = detect_plate("camera/car.jpg")
            plate = plate.json()

            logging.info("Resposta recebida pelo modelo identificador de placas.")
            logging.info(f"Placa identificado: {plate}")

            api_url = os.getenv('API_URL')

            token = get_token(credentials_file_path)

            headers = { 'Authorization': token }
            payload = {
                'plate': plate
            }

            logging.info("Verificando se o veículo está cadastrado no sistema.")
            response = get(api_url, '/search/vehicle_by_plate', payload, headers)

            vehicle = response.json()

            if response.status_code == 200:
                logging.info(f"Veículo \"{vehicle['nickname']}\" encontrado para cliente com ID {vehicle['client_id']}.")

                entry_date = datetime.utcnow()
                exit_date = entry_date + timedelta(hours=2)

                entry_date_string = entry_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                exit_date_string = exit_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

                payload = {
                    'movement': {
                        'client_id': vehicle['client_id'],
                        'vehicle_id': vehicle['id'],
                        'entry': entry_date_string,
                        'exit': exit_date_string,
                        'cost': 6
                    }
                }

                logging.info(f"Criando movimentação para {payload['movement']['client_id']} com custo {payload['movement']['cost']}.")

                response = post(api_url, '/movements', payload, headers)

                # Abrindo a cancela
                barrier.open()

                while (barrier.vehicle_is_near()):
                    barrier.loading_signal()
                    logging.info("Aguardando veículo atravessar...")
                    time.sleep(0.5)

                time.sleep(9)

                barrier.close()


            if response.status_code == 404:
                logging.info(f"Não foi possível encontrar veículo com placa \"{plate}\".")
                barrier.warning_led.on()
                time.sleep(3)
                continue

        print(f"Distância do veículo: {barrier.presence_sensor.measure_distance()}")

def main():
    try:
        barrier = setup()
        loop(barrier)

    except KeyboardInterrupt:
        logging.info("Programa interrompido pelo usuário.")

    finally:
        logging.info("Liberando canais do controlador.")
        GPIO.cleanup()
        logging.info("Aplicação encerrada.")


if __name__ == '__main__':
    main()
