import json
import os

def load_configs(root_dir):
  try:
    config_file_path = os.path.join(root_dir, "config.json")

    with open(config_file_path) as config_file:
      configs = json.load(config_file)
      actuator_pin = configs["actuator"]["pin"]
      warning_led_pin = configs["leds"]["warning"]
      success_led_pin = configs["leds"]["success"]

      if actuator_pin and warning_led_pin and success_led_pin:
        return {
          "actuator": {
            "pin": actuator_pin
          },
          "leds": {
            "warning": warning_led_pin,
            "success": success_led_pin
          }
        }

      print("Algum campo não foi fornecido")
      return None

  except FileNotFoundError:
    print("Arquivo não encontrado")
    return None
