import RPi.GPIO as GPIO
import time 

servo = 19 #servo pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)
pwm = GPIO.PWM(servo, 50)
pwm.start(0)

switch = 13 # pin
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
trip = GPIO.input(switch)


#DRY IS 1; WET IS 0


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
    
def sonarSensor(): ########################
    
    TRIG = 21
    ECHO = 20
    GPIO.setmode(GPIO.BCM)
    
    while True:
        print("distance measurement in progress")
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.output(TRIG, False)
        
        print("waiting for sensor to settle")
        time.sleep(0.2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
            
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 740               ###17150 for air, 740 water
        distance = round(distance, 2)
        print("distance: ", distance, "cm")
        
        time.sleep(2)  
        
        return distance


#takes water in until it hits switch at the top
def waterIn():                          ###turn counterclockwise

    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(servo,GPIO.OUT)
    #pwm = PWM.GPIO(servo, 50)
    #pwm.start()
    print("activating servo up")
  
    
    trip = GPIO.input(switch)

    if (trip == 0):
            pwm.ChangeDutyCycle(4)
            
    while GPIO.input(switch) == 0:
        pass
    
    pwm.ChangeDutyCycle(0)
        #1 means switch activated
        #0 means not
        
        #if (trip == 0):
         #   pwm.ChangeDutyCycle(5)
       # else:
        #    pwm.ChangeDutyCycle(0)
        #    i = i + 1
       # pwm.ChangeDutyCycle(5)
    
def waterOut():                         ###turn clockwise

    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(servo,GPIO.OUT)
    #pwm = PWM.GPIO(servo, 50)
    #pwm.start()
    trip = GPIO.input(switch)
    print ("trip = ", trip)
    if (trip == 1):
        pwm.ChangeDutyCycle(10)
        print("activating servo down")
        time.sleep(33)
        pwm.ChangeDutyCycle(0)
    

    
# while 1:
    
#servo begins the program at the top of the syringe, so there is a forced
#waterIn() then waterOut()
#start by water out

def main():
    
    count = 0
    
    #sinks down when deployed
    #goes up
    # COUNT = 1 - goes down
    #goes up
    # COUNT = 2 - goes down
    
#while (count < 3):
    for _ in range(3):
        while sonarSensor() > 3:
            print("going down")
            
        waterOut()    
            
        while liquidSensor() == 0:
            print("going up")
        
        waterIn()
            
       
    #GPIO.cleanup()
   


#while True:
    #waterOut()
    
waterIn() #check that the syringe is completely empty
time.sleep(2)
waterOut()
    #engine now @ top of pool
while (liquidSensor() == 0):
    #time.sleep()
    pass #doesn't do anything

while (liquidSensor() == 1):                            #starts plunger @ bottom
    pass 

waterIn()      #starts going down
while (liquidSensor() == 1):
    pass
time.sleep(5)
print("running main")
main()
waterOut()

GPIO.cleanup()
