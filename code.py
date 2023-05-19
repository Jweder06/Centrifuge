from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import motor as Motor
input 
DEBUG = False  # mode of operation; False = normal, True = debug
OP_DURATION = 5  # operation duration in seconds
drv8833_ain1 = PWMOut(board.D8, frequency=50)
drv8833_ain2 = PWMOut(board.D9, frequency=50)
drv8833_bin1 = PWMOut(board.D12, frequency=50)
drv8833_bin2 = PWMOut(board.D11, frequency=50)
button_a = DigitalInOut(board.D7)
drv8833_sleep = DigitalInOut(board.D5)
motor_a = Motor.DCMotor(drv8833_ain1, drv8833_ain2)
button_a.direction = Direction.INPUT
button_a.pull = Pull.UP
def basic_operations():
    if button_a.value:  
        bumotor_a.throttle = 1.0
    print(button_a.value)
drv8833_sleep.direction = Direction.OUTPUT
drv8833_sleep.value = True  # enable (turn on) the motor driver
if DEBUG: print("Running in DEBUG mode.  Turn off for normal operation.")
while True:
    basic_operations()  # perform basic motor control operations on motor A