from gpiozero import AngularServo, Button
from time import sleep

b1 = Button(2)
b2 = Button(3)


servo = AngularServo(17, min_angle=-80, max_angle = 80)

while True:
    if b1.is_pressed:
        servo.angle = 70
    elif b2.is_pressed:
        servo.angle =-70
    else:
        servo.angle = 0  