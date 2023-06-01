#type: ignore
from time import sleep      #importing Libraries
from PID_CPY import PID
import time
import math
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import motor as Motor
pid = PID(-1, -0.5, -0.15, setpoint= .8 )  #Setting PID values
pid.output_limits = (.2,1)      #Limiting output values
throttle = .2                #Seting starting throttle
led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT
photoI = digitalio.DigitalInOut(board.D6)
photoI.direction = digitalio.Direction.INPUT
photoI.pull = digitalio.Pull.UP
Bvalue = False      #declaring variables
AverageT = 0
RPM= 0
Tcount = 0
Processed = True
Diffrence = 0
Currenttime = 0
Pasttime = 0
Interupts = 0
drv8833_ain1 = PWMOut(board.D8, frequency=50)       #DRV8833
drv8833_ain2 = PWMOut(board.D9, frequency=50)
drv8833_bin1 = PWMOut(board.D12, frequency=50)
drv8833_bin2 = PWMOut(board.D11, frequency=50)
button_a = DigitalInOut(board.D7)
drv8833_sleep = DigitalInOut(board.D5)
motor_a = Motor.DCMotor(drv8833_ain1, drv8833_ain2)
button_a.direction = Direction.INPUT
button_a.pull = Pull.UP
drv8833_sleep.direction = Direction.OUTPUT
drv8833_sleep.value = True                                # enable (turn on) the motor driver
buttonstate="not pressed"
while True:
    if button_a.value == 0 and buttonstate == "not pressed": 
        Bvalue = not Bvalue
        buttonstate = "pressed"     #debounce for button
    elif button_a.value == 1: 
        buttonstate = "not pressed"     #debounce for button
    if Bvalue == True:
        motor_a.throttle = 1 #throttle     #motor on
        led.value = True       #Power LED ON          
    
    elif Bvalue == False:
        motor_a.throttle = 0    
        led.value = False       #Power LED Off                    
    Truetime = time.monotonic()
  if photoI.value == True and Processed == True:       # Encoder
        Currenttime = Truetime      #Records the current interupt time
        Diffrence = Currenttime - Pasttime      #finds the diffrence
        Pasttime = Currenttime      #It knows current interupt has been recored so it sets current to past interupt
        Processed = False       #debounce
        Tcount = Tcount + 1     #counts the cycles for average
    if photoI.value == False:
        AverageT = AverageT + Diffrence     #Adds the difrence up 5 times
        Processed = True
    if Tcount == 5:
        AverageT = AverageT/6                           #Avarge count and print
       # print("Perod:", RPM )
        Tcount = 0
        AverageT = Diffrence
        print("throttle:", throttle )
        print("RPM:", RPM )
        print((throttle,RPM,.8))
    if AverageT == 0:
        AverageT =.1
    RPM=60/(AverageT * 3)
    throttle = pid(RPM)
