import RPi.GPIO as GPIO
import time


led_pin = 12


def setup():
    # set up board
    GPIO.setmode(GPIO.BOARD)
    # set pins
    GPIO.setup(led_pin, GPIO.OUT)
    turn_off()


def cleanup():
    GPIO.cleanup()


def turn_on():
    GPIO.output(led_pin, 1)


def turn_off():
    GPIO.output(led_pin, 0)


def blink():
    for i in range(10):
        if i % 2 == 0:
            turn_on()
        else:
            turn_off()
        time.sleep(.25)
    turn_off()


def fade():
    p = GPIO.PWM(led_pin, 50)
    for i in range(5):
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
    p.stop()

