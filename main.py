from time import sleep

import digitalio as DIO

coils =[
    DIo.DigitalInOut(board.D8),  # A1
    DIo.DigitalInOut(board.D9),  # A2
    DIo.DigitalInOut(board.D10),  # B1
    DIo.DigitalInOut(board.D11),  # B2
    ]
for coil in coils:
    coil.direction = DIo.Direction.OUTPUT

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)



while True:
    print("Hello world!")
    sleep(1)