from time import sleep
import time
import board
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import motor as Motor
Bvalue = False
drv8833_ain1 = PWMOut(board.D8, frequency=50)
drv8833_ain2 = PWMOut(board.D9, frequency=50)
drv8833_bin1 = PWMOut(board.D12, frequency=50)
drv8833_bin2 = PWMOut(board.D11, frequency=50)
button_a = DigitalInOut(board.D7)
drv8833_sleep = DigitalInOut(board.D5)
motor_a = Motor.DCMotor(drv8833_ain1, drv8833_ain2)
button_a.direction = Direction.INPUT
button_a.pull = Pull.UP
drv8833_sleep.direction = Direction.OUTPUT
drv8833_sleep.value = True  # enable (turn on) the motor driver
buttonstate="not pressed"
print("helllo world")
while True:
    print(Bvalue)
    if button_a.value == 0 and buttonstate == "not pressed": 
        Bvalue = not Bvalue
        buttonstate = "pressed"
    elif button_a.value == 1: 
        buttonstate = "not pressed"
    if Bvalue == True:
            motor_a.throttle = 1
    elif         

   