import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        time.sleep(0.1)

        self.off()

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
