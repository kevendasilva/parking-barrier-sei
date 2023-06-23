import RPi.GPIO as GPIO
import time

from barrier.led import Led

# Define o pino GPIO a ser usado
pin = 3

warning_led = Led(pin = pin)

# Configuração dos pinos GPIO


# Piscar o LED 10 vezes
for i in range(10):
    warning_led.on()  # Liga o LED
    time.sleep(1)                # Espera 1 segundo
    warning_led.off()   # Desliga o LED
    time.sleep(1)                # Espera 1 segundo

# Limpeza dos pinos GPIO
GPIO.cleanup()
