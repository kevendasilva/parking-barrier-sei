import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Actuator:
    def __init__(self, pin, initial_position):
        self.pin = pin

        GPIO.setup(pin, GPIO.OUT)
        self.set_position(initial_position)

    def set_position(self, duty_cycle):
        pwm = GPIO.PWM(self.pin, 50)
        time.sleep(0.3)
        pwm.start(duty_cycle)
        time.sleep(0.3)
        pwm.stop()
