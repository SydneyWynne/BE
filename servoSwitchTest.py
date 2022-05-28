import RPi.GPIO as GPIO
import time

servo = 19 #servo pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)
pwm = GPIO.PWM(servo, 50)
pwm.start(0)

switch = 13 #pin
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#i = 0

while 1:
    trip = GPIO.input(switch)
    if (trip == 0):
        pwm.ChangeDutyCycle(5)
        print("going up")
    else:
        pwm.ChangeDutyCycle(10)
        print("done")
        #i= i+ 1
   
    
pwm.stop()
GPIO.cleanup()