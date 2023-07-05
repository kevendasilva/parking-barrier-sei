import json
import os

def load_configs(root_dir):
  try:
    config_file_path = os.path.join(root_dir, "config.json")

    with open(config_file_path) as config_file:
      configs = json.load(config_file)
      actuator_pins = configs["actuator"]["pins"]
      warning_led_pin = configs["leds"]["warning"]
      success_led_pin = configs["leds"]["success"]
      trigger_pin = configs["presence_sensor"]["trigger_pin"]
      echo_pin = configs["presence_sensor"]["echo_pin"]

      if actuator_pins and warning_led_pin and success_led_pin and trigger_pin and echo_pin:
        return {
          "actuator": {
            "pins": actuator_pins
          },
          "leds": {
            "warning": warning_led_pin,
            "success": success_led_pin
          },
          "presence_sensor": {
            "trigger_pin": trigger_pin,
            "echo_pin": echo_pin
          }
        }

      print("Algum campo não foi fornecido")
      return None

  except FileNotFoundError:
    print("Arquivo não encontrado")
    return None
