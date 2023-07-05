import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Barrier:
    DISTANCE_LIMIT = 100
    DISTANCE_LIMIT_MARGIN_ERROR = 50
    VEHICLE_IS_NEAR_TEST = 3

    def __init__(self, actuator, warning_led, success_led, presence_sensor):
        self.actuator = actuator
        self.warning_led = warning_led
        self.success_led = success_led
        self.presence_sensor = presence_sensor
        self.vehicle_is_near_count = 0
        self.first_attempt = time.time()

    def loading_signal(self, delay = 0.3):
        self.warning_led.on()
        self.success_led.on()
        time.sleep(delay)
        self.warning_led.off()
        self.success_led.off()
        time.sleep(delay)

    def error_signal(self, delay = 0.3):
        self.warning_led.on()
        time.sleep(delay)
        self.warning_led.off()
        self.sleep(delay)

    def open(self):
        self.actuator.right(128)
        time.sleep(0.5)

    def close(self):
        self.actuator.left(128)
        time.sleep(0.5)

    def vehicle_is_near(self):
        distance = self.presence_sensor.measure_distance()

        lower_distance_limit = self.DISTANCE_LIMIT - self.DISTANCE_LIMIT_MARGIN_ERROR
        upper_distance_limit = self.DISTANCE_LIMIT + self.DISTANCE_LIMIT_MARGIN_ERROR
        distance_is_between_limit = lower_distance_limit <= distance and distance <= upper_distance_limit

        elapsed_time = time.time() - self.first_attempt

        if distance_is_between_limit:
            self.vehicle_is_near_count += 1
            self.first_attempt = time.time()

        if elapsed_time >= 3:
            self.vehicle_is_near_coutn = 0

        if self.vehicle_is_near_count == self.VEHICLE_IS_NEAR_TEST:
            self.vehicle_is_near_count = 0
            return True

        return False
