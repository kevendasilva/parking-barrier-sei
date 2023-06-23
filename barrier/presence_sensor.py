import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class PresenceSensor:
    ROUNDS_THE_DISTANCE_TO = 2
    SPEED_OF_SOUND = 34300

    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)

    def measure_distance(self):
        GPIO.output(self.trigger_pin, GPIO.LOW)
        time.sleep(0.5)

        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, GPIO.LOW)

        while GPIO.input(self.echo_pin) == GPIO.LOW:
            pulse_start = time.time()

        while GPIO.input(self.echo_pin) == GPIO.HIGH:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * self.SPEED_OF_SOUND / 2
        distance = round(distance, self.ROUNDS_THE_DISTANCE_TO)

        return distance
