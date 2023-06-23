import os
import RPi.GPIO as GPIO
import time

from barrier.actuator import Actuator
from barrier.led import Led
from barrier.presence_sensor import PresenceSensor
from barrier.utils.load_configs import load_configs

def setup():
  configs = load_configs(root_dir = os.getcwd())

  actuator = Actuator(pin = configs["actuator"]["pin"], initial_position = 10)
  warning_led = Led(pin = configs["leds"]["warning"])
  success_led = Led(pin = configs["leds"]["success"])

def main():
    try:
        setup()
        ps = PresenceSensor(trigger_pin = 24, echo_pin = 23)

        while True:
            distance = ps.measure_distance()
            print(f"Distância: {distance} cm")
            time.sleep(0.3)

    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário")

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
