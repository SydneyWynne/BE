import RPi.GPIO as GPIO
import time 


def liquidSensor(): #########################

    sensorOut = 7

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensorOut, GPIO.IN)

    while True:
        isDry = GPIO.input(sensorOut)
        if (isDry):
            print("dry")
            return 1 
        else:
            print("wet")
            return 0
        
    time.sleep(3)
  
while 1:
    liquidSensor()