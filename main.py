import os
import RPi.GPIO as GPIO
import time
import requests

from barrier.actuator import Actuator
from barrier.barrier import Barrier
from barrier.led import Led
from barrier.presence_sensor import PresenceSensor
from barrier.utils.load_configs import load_configs

def setup():
  configs = load_configs(root_dir = os.getcwd())

  actuator = Actuator(6, 13, 19, 26)
  time.sleep(1)

  warning_led = Led(pin = configs["leds"]["warning"])
  success_led = Led(pin = configs["leds"]["success"])
  presence_sensor = PresenceSensor(trigger_pin = configs["presence_sensor"]["trigger_pin"], echo_pin = configs["presence_sensor"]["echo_pin"])

  barrier = Barrier(actuator, warning_led, success_led, presence_sensor)

  return barrier

def loop(barrier):
    while True:
        if (barrier.vehicle_is_near()):
            print("Carro está próximo.")

            url = 'http://3.92.136.209/api/detect-plate/v1/'  # Replace with your AWS Public IP
            image_file = 'camera/car.jpg'

            headers = {'accept': 'application/json'}
            files = {'img_file': open(image_file, 'rb')}

            response = requests.post(url, headers=headers, files=files)

            print(response.json())


def main():
    try:
        barrier = setup()
        loop(barrier)

    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário")

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
