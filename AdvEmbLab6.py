from gpiozero import DistanceSensor
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

sensor = DistanceSensor(23, 24)
while True:
 print('Distance to nearest object is', sensor.distance, 'm')
 if sensor.distance >  0.5:
    GPIO.output(12, True)
    print("hisadoah")
    sleep(0.5)
 sleep(1)