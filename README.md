# Centrifuge

This is a simple centrifuge using PID to control the speed of the centrifuge. The goal is to be able to get the PID to get to a certin speed and if time allows a rotary encoder will be used to change the goal speed

## Planing

Most of the planning was done in a simple MS paint where the layout of the project was set and the functions of each sensor was thought out.

<img src="https://user-images.githubusercontent.com/112961442/235988539-00ad7e6e-b546-4868-ab20-6a5bdbae56b4.png" width="700">

### Schedule 


<img src="https://github.com/Jweder06/Centrifuge/assets/112961442/e35dd01f-ac83-45e9-8f0b-2598dc76df01" width="700">

<img src="https://github.com/Jweder06/Centrifuge/assets/112961442/7989c4ea-bb1d-4536-8126-3188b0f3ec00" width="400">

# CAD
https://cvilleschools.onshape.com/documents/14cd3189dba3e8f19700045c/w/aa40a4c4bcfc04fb935ae4f6/e/0377bc9ccd1a3051eb0eb9a7?renderMode=0&uiState=6479f1f7d061192a0c3c4185
This was some of the simplest cad work I have done and required simple mounts and a simple acrylic box that was made in less than a week of CAD work. The goal was to make a simple streamlined design that would allow for easy construction. One element of that is that the walls are independent of the base except for the brackets making it easy to wire test and then place the walls. If the parts were integrated into the walls the assembly would be much more difficult.

### Vials and holder


<img src="https://user-images.githubusercontent.com/112961442/234093672-1a8a80b8-5776-44bb-97e3-00ad02e57296.png" width="700">

The vials where made with 3d lines, filled into a surface and the cut to make the vial. That was then transformed into the holder and booleand into the cone to make the vial holder. Finaly the part was lightened to make it cheaper to print and easier to spin up to high speed becasue of a reduced weight.

### Making the mount

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/acd4d081-f7b9-45ae-9121-f1c187261d83" width="700">

Although this was a quick job and initially was thought to be a bad design it turned out to be do great job as it was very easy to remove the motor to work on the wires. It worked by having pegs go through the bolt holes but not be too tight to create a friction fit.

### Standardization

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/19f2202f-2c6a-4c81-8ec9-c65bf08bc994" width="700">

This is another example of me trying to standardize my designs across the board. I do this so creating future projects is not reinventing parts over and over again and so I reiterate when I need to make my parts even better making each version better through every new project not just once.

### Making space for easy access

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/1f072a36-546b-4845-9548-c2e2e1377c85" width="700">

For my design, I tried to keep in mind the difficulties of construction and so I made sure to keep lots of space for wiring and electronics. I knew that a DRV8833 requires direct Arduino pin access so I placed a breadboard next to the Arduino to make sure it fit.

# Construction

### Electonics and Wiring

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/88a62308-7464-4afd-855b-c6805dd8ad9e" width="700">

This is a wiring diagram made on frizing for the circut of the entire centrifuge it inclues everything needed for the project. I made this before wired my project and used it as a refrence allthough I didnt copy exact pin numbers.

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/c4e738bb-f499-446f-b62f-294b7545bca9" width="700">
Real life circut image

### Redoing the Wiring

<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/78947384-c0b3-4f0b-a154-cceb28b60636" width="700">

To get an exact fit for my photointeruper I had to make sure that the drill holes within the acrylic base were exact. because the previous existing drill holes were created for the stepper mount they needed to be redrilled and my wiring need to be redone on a new sheet of acrylic this was a pain as I had to rip off breadboards that then broke and so I needed to rewire almost the entire project.

### Stepper Motor

<img src="https://github.com/Jweder06/Centrifuge/assets/112961442/67cfb86a-e536-4af0-bb73-54225bb4cba8" width="700">

At the very beginning of my project, I planned to use a stepper motor because of a miscommunication with my teacher. I should have known that you can't use stepper motors for PID since they're too exact, but I didn't and so I had to replace the entire motor system which took a few days of redesigning and rewiring.

### Drilling

<img src="https://github.com/Jweder06/Centrifuge/assets/112961442/7cd4723d-4788-4bff-a730-1f11c6d5f82e" width="700">

Before I replaced the bottom plate I attempted to drill new holes for the TT motor holder manually. This was a complete waste of time as my holes would never be exact enough to get the perfect fit that I needed. I spent a lot of time attempting to mark the perfect location for a drill hole that inevitably would be off by a few millimeters. Through this I learned that for exact fits its better to get the laser cutter to do it.

### Photo interrupter interrupts


<img src="https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/6813e4b9-9d72-4af4-9a39-600d7eb20606" width="700">

 The photo interrupter had by far the largest issue its counting in the encoder code was inconsistent at high speeds and it would detect part going through it but the code wouldn't have enough time to count it.  because the main goal of the project was to go as fast as possible but still being PID  meant that I couldn't compromise on the speed therefore I had to do a lot of testing on how to allow the photo interrupter to still detect being interrupted even at high speeds.  this was done by changing the part that goes through the photo interrupter and making it bigger. This allows the code to run while the photo interrupter is still interrupted meaning we can accurately count.
 
### Bill of matirials 
<img src="https://github.com/Jweder06/Centrifuge/assets/112961442/876aa3f5-f8fd-490b-8a72-27315373aa3e" width="700">

# Code
```python
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
        AverageT = AverageT/6       #Averages the counted total
       # print("Perod:", RPM )
        Tcount = 0      # Rests count
        AverageT = Diffrence        #Rests average for the next count
        print("throttle:", throttle )
        print("RPM:", RPM )
        print((throttle,RPM,.8))        #Plotting
    if AverageT == 0:
        AverageT =.1
    RPM=60/(AverageT * 3)
    throttle = pid(RPM)     #PID

```
### Debounce button

A debouncer is a part of code that only allows a button to be pressed once. It does this by confirming that the button has been released before lawing another press to be registered.This was a semi-reintroduction into Python code and by having others help me learn how to write a debouncer I regained a lot of Python knowledge.

```python
    if button_a.value == 0 and buttonstate == "not pressed": 
        Bvalue = not Bvalue
        buttonstate = "pressed"     #debounce for button
    elif button_a.value == 1: 
        buttonstate = "not pressed"     #debounce for button
    if Bvalue == True:
        motor_a.throttle = throttle     #motor on
        led.value = True       #Power LED ON          
    
    elif Bvalue == False:
        motor_a.throttle = 0    
        led.value = False       #Power LED Off     
```
I used this debouncer to debounce a button controlling the motor's on-off state.
### Encoder

An encoder is part of the PID process that records the speed of the motor to help the PID control the throttle. My encoder worked by debouncing a photo interrupter and then every time it is interrupted record a time then subtract the difference between the current interrupt and the time before it, giving the time between each Interrupt. This value is then calculated into RPM by dividing 60 by the period in seconds. 

```python
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
        AverageT = AverageT/6       #Averages the counted total
        Tcount = 1                  # Rests count
        AverageT = Diffrence        #Rests average for the next count
```
This value was fed into the PID as the input

### PID
```python
from PID_CPY import PID

pid = PID(-1, -0.5, -0.15, setpoint= 1.5 )  #Setting PID values
pid.output_limits = (.2,1)      #Limiting output values
throttle = .2                #Seting starting throttle

while True:
throttle = pid(Period)
```
The hardest part about PID was definitely the tuning it required a lot of tweaking to get even to a basic state and even more tuning to get it to a more finalized version with fewer oscillations. This was Exceptionally difficult as I didn't know which PID values changed which part of the PID graph.

### Averaging

This section of code counts the diffrence 5 times and then devides them by 5 getting the avarge value. This helps create a smother PID as it has less values to go through and each value is more generalized causing it to be easier to reach the setpoint.

```python
    if Tcount == 5:
        AverageT = AverageT/6       #Averages the counted total
        Tcount = 0      # Rests count
        AverageT = Diffrence        #Rests average for the next count
        print("throttle:", throttle )
        print("RPM:", RPM )
        print((throttle,RPM,.8))        #Plotting
    if  AverageT == 0:
        AverageT =.1
```
## Final Project

(instert video here)

The final project was a success the PID worked mostly, with a semi oscillating PID and a working control system and well-costructed box

# Reflection
This project taught me an incredible amount, I went from being completely Python-incompetent to being semi-competent. I have to attribute this growth to all the help I received from my teachers and classmates(Yes even Graham. G). I was able to code my own encoder, debounced button, and even PID. I now realized that I learned so much because I didn't take the easy route of copypasta, I tried to code it myself learning a lot on the way. I also applied a few of the time management skills I learned in the last project making the project simple and implementing a lot of planning structures making it easier to finish documentation and my project simultaneously. I think what I need to work on is communication, I wanted a partner and really needed one but I went down the flawed path of solo projects The place where all unfinished projects live) wich harmed y potential for an even more polished project.