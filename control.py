#!/usr/bin/env python3
"""
Receives Morse code input and transmits via LED
"""

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Unable to import GPIO library")
    print("Missing library, or not running as root")
    exit()
import time

GPIO.setwarnings(False)
led = 23 # set LED anode pin number
GPIO.setmode(GPIO.BOARD) # set GPIO pin numbers to board mode
GPIO.setup(led, GPIO.OUT) # set anode pin to output mode
unit = 0.2 # define base Morse unit length

def blink(signal):

    if signal == ".":
        GPIO.output(led, 1) # activate LED
        time.sleep(unit)
        GPIO.output(led, 0) # disable LED
        time.sleep(unit)
    elif signal == "-":
        GPIO.output(led, 1) # activate LED
        time.sleep(unit*3)
        GPIO.output(led, 0) # disable LED
        time.sleep(unit)

