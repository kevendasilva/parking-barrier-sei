import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class Actuator:
    def __init__(self, IN1, IN2, IN3, IN4):
        self.IN1 = IN1
        self.IN2 = IN2
        self.IN3 = IN3
        self.IN4 = IN4

        GPIO.setup(IN1, GPIO.OUT)
        GPIO.setup(IN2, GPIO.OUT)
        GPIO.setup(IN3, GPIO.OUT)
        GPIO.setup(IN4, GPIO.OUT)

        GPIO.output(IN1, False)
        GPIO.output(IN2, False)
        GPIO.output(IN3, False)
        GPIO.output(IN4, False)

        self.time = 0.001

    def Step1(self):
        GPIO.output(self.IN4, True)
        sleep(self.time)
        GPIO.output(self.IN4, False)

    def Step2(self):
        GPIO.output(self.IN4, True)
        GPIO.output(self.IN3, True)
        sleep(self.time)
        GPIO.output(self.IN4, False)
        GPIO.output(self.IN3, False)

    def Step3(self):
        GPIO.output(self.IN3, True)
        sleep(self.time)
        GPIO.output(self.IN3, False)

    def Step4(self):
        GPIO.output(self.IN2, True)
        GPIO.output(self.IN3, True)
        sleep(self.time)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, False)

    def Step5(self):
        GPIO.output(self.IN2, True)
        sleep(self.time)
        GPIO.output(self.IN2, False)

    def Step6(self):
        GPIO.output(self.IN1, True)
        GPIO.output(self.IN2, True)
        sleep(self.time)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)

    def Step7(self):
        GPIO.output(self.IN1, True)
        sleep(self.time)
        GPIO.output(self.IN1, False)

    def Step8(self):
        GPIO.output(self.IN4, True)
        GPIO.output(self.IN1, True)
        sleep(self.time)
        GPIO.output(self.IN4, False)
        GPIO.output(self.IN1, False)

    def left(self, step):
        for i in range (step):
            self.Step1()
            self.Step2()
            self.Step3()
            self.Step4()
            self.Step5()
            self.Step6()
            self.Step7()
            self.Step8()

    def right(self, step):
        for i in range (step):
            self.Step8()
            self.Step7()
            self.Step6()
            self.Step5()
            self.Step4()
            self.Step3()
            self.Step2()
            self.Step1()
