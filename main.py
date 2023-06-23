import os
import RPi.GPIO as GPIO
import time

from barrier.actuator import Actuator
from barrier.led import Led
from barrier.utils.load_configs import load_configs

def setup():
  configs = load_configs(root_dir = os.getcwd())

  actuator = Actuator(pin = configs["actuator"]["pin"], initial_position = 0)
  warning_led = Led(pin = configs["leds"]["warning"])
  success_led = Led(pin = configs["leds"]["success"])

setup()

GPIO.cleanup()
