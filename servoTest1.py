import RPi.GPIO as GPIO
import time 

servo = 19 #servo pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)

pwm = GPIO.PWM(servo, 50)
pwm.start(0)
while 1:
    x = int (input("value?"))
    pwm.ChangeDutyCycle(x) #counter/up
    time.sleep(2)
#pwm.ChangeDutyCycle(10) #clockwise/down
#time.sleep(2)
pwm.stop()
GPIO.cleanup()