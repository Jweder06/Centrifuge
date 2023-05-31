# Centrifuge

This is a simple centrifuge using PID to control the speed of the centrifuge. The goal is to be able to get the PID to get to a certin speed and if time allows a rotary encoder will be used to change the goal speed

## Planing

Most of the planning was done in a simple MS paint where the layout of the project was set and the functions of each sensor was thought out.

![image](https://user-images.githubusercontent.com/112961442/235988539-00ad7e6e-b546-4868-ab20-6a5bdbae56b4.png)

### Schedule 

![images needed](https://github.com/Jweder06/Cad/assets/112961442/fbf0d0ce-a4a2-468d-aa35-59163645e635)

## CAD

This was some of the simplest cad work I have done and required simple mounts and a simple acrylic box that was made in less than a week of CAD work. The goal was to make a simple streamlined design that would allow for easy construction. One element of that is that the walls are independent of the base except for the brackets making it easy to wire test and then place the walls. If the parts were integrated into the walls the assembly would be much more difficult.

### Vials and holder

![image](https://user-images.githubusercontent.com/112961442/234093672-1a8a80b8-5776-44bb-97e3-00ad02e57296.png)

The vials where made with 3d lines, filled into a surface and the cut to make the vial. That was then transformed into the holder and booleand into the cone to make the vial holder. Finaly the part was lightened to make it cheaper to print and easier to spin up to high speed becasue of a reduced weight.

### Making the mount

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/acd4d081-f7b9-45ae-9121-f1c187261d83)

Although this was a quick job and initially was thought to be a bad design it turned out to be do great job as it was very easy to remove the motor to work in the wires.

### Standardization

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/19f2202f-2c6a-4c81-8ec9-c65bf08bc994)

This is another example of me trying to standardize my designs across the board. I do this so creating future projects is not reinventing parts over and over again and so I reiterate when I need to make my parts even better making each version better through every new project not just once.

### Making space for easy access

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/1f072a36-546b-4845-9548-c2e2e1377c85)

For my design, I tried to keep in mind the difficulties of construction and so I made sure to keep lots of space for wiring and electronics. I knew that a DRV8833 requires direct Arduino pin access so I placed a breadboard next to the Arduino to make sure it fit.

## Electonics and placement
<img src="https://user-images.githubusercontent.com/112961442/236470311-b8f9e0b9-ef88-4ae0-98ef-ff99ea000287.png" alt="image"/>![image](https://user-images.githubusercontent.com/112961442/236893396-dd29db23-5f42-482f-acd0-c983642e0922.png)

Use import pull up for button 
## Construction

### Electonics and Wiring

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/88a62308-7464-4afd-855b-c6805dd8ad9e)

This is a wiring diagram made on frizing for the circut of the entire centrifuge it inclues everything needed for the project. I made this before wired my project and used it as a refrence allthough I didnt copy exact pin numbers.

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/c4e738bb-f499-446f-b62f-294b7545bca9)

Real life circut image

### Redoing the Wiring

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/78947384-c0b3-4f0b-a154-cceb28b60636)

To get an exact fit for my photointeruper I had to make sure that the drill holes within the acrylic base were exact. because the previous existing drill holes were created for the stepper mount they needed to be redrilled and my wiring need to be redone on a new sheet of acrylic this was a pain as I had to rip off breadboards that then broke and so I needed to rewire almost the entire project.

### Stepper Motor

![images needed](https://github.com/Jweder06/Cad/assets/112961442/fbf0d0ce-a4a2-468d-aa35-59163645e635)

At the very beginning of my project, I planned to use a stepper motor because of a miscommunication with my teacher. I should have known that you can't use stepper motors for PID since they're too exact, but I didn't and so I had to replace the entire motor system which took a few days of redesigning and rewiring.

### Drilling

![images needed](https://github.com/Jweder06/Cad/assets/112961442/fbf0d0ce-a4a2-468d-aa35-59163645e635)

Before I replaced the bottom plate I attempted to drill new holes for the TT motor holder manually. This was a complete waste of time as my holes would never be exact enough to get the perfect fit that I needed. I spent a lot of time attempting to mark the perfect location for a drill hole that inevitably would be off by a few millimeters. Through this I learned that for exact fits its better to get the laser cutter to do it.

### Photo interrupter interrupts

![image](https://github.com/Jweder06/Paper-air-plane-launcher/assets/112961442/6813e4b9-9d72-4af4-9a39-600d7eb20606)

 The photo interrupter had by far the largest issue its counting in the encoder code was inconsistent at high speeds and it would detect part going through it but the code wouldn't have enough time to count it.  because the main goal of the project was to go as fast as possible but still being PID  meant that I couldn't compromise on the speed therefore I had to do a lot of testing on how to allow the photo interrupter to still detect being interrupted even at high speeds.  this was done by changing the part that goes through the photo interrupter and making it bigger. This allows the code to run while the photo interrupter is still interrupted meaning we can accurately count.

## Code

### Debounce button

### Encoder

### PID

## Reflection
