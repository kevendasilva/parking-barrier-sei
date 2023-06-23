import time
import os

from barrier.actuator import Actuator
from barrier.utils.load_configs import load_configs

def setup():
  configs = load_configs(root_dir = os.getcwd())

  actuator = Actuator(pin = configs["actuator"]["pin"], initial_position = 5)

setup()
time.sleep(3)
