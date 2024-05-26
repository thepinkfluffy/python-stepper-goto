import RPi.GPIO as GPIO
import time

step = 15
direction = 14
en = 21
ms3 =24
ms2 =25
ms1 =8
step2 = 23
dir2 = 18
#enable2=14
def anglesToSteps(alpha,stp):
	return((2**(stp-1))*alpha/1.8)


GPIO.setmode(GPIO.BCM)

GPIO.setup(step,GPIO.OUT)
GPIO.setup(direction,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.setup(ms3,GPIO.OUT)
GPIO.setup(ms2,GPIO.OUT)
GPIO.setup(ms1,GPIO.OUT)

GPIO.setup(step2,GPIO.OUT)
GPIO.setup(dir2,GPIO.OUT)
#GPIO.setup(enable2,GPIO.OUT)

#GPIO.setup(ms3_2,GPIO.OUT)
#GPIO.setup(ms2_2,GPIO.OUT)
#GPIO.setup(ms1_2,GPIO.OUT)
def disable(x):
	if(x==1):
		GPIO.output(en,GPIO.HIGH)
	else:
		raise Exception("yo that shit aint good|number has to be between 1 and 3 ")
def enable(x):
	if(x==1):
		GPIO.output(en,GPIO.LOW)
	else:
		raise Exception("yo that shit aint good|number has to be between 1 and 3 ")

def move(Direction,Speed,Motor,StepsPerSec,degrees):
	#steps to degrees 
	#1 full step = 1.8
	steps = anglesToSteps(degrees,Speed)
	print(degrees,steps)
	enable(1)
	if(Speed==1):#full
			GPIO.output(ms1,GPIO.LOW)
			GPIO.output(ms2,GPIO.LOW)
			GPIO.output(ms3,GPIO.LOW)
	elif(Speed==2):#half
			GPIO.output(ms1,GPIO.HIGH)
			GPIO.output(ms2,GPIO.LOW)
			GPIO.output(ms3,GPIO.LOW)
	elif(Speed==3):#quarter
			GPIO.output(ms1,GPIO.LOW)
			GPIO.output(ms2,GPIO.HIGH)
			GPIO.output(ms3,GPIO.LOW)
	elif(Speed==4):#eight
			GPIO.output(ms1,GPIO.HIGH)
			GPIO.output(ms2,GPIO.HIGH)
			GPIO.output(ms3,GPIO.LOW)
	elif(Speed==5):#sixteenth
			GPIO.output(ms1,GPIO.HIGH)
			GPIO.output(ms2,GPIO.HIGH)
			GPIO.output(ms3,GPIO.HIGH)
	else:
			raise Exception("number has to be between 1 and 5")
		
	if(Motor == 1):
		if(Direction == 1):
			GPIO.output(direction,GPIO.HIGH)
		elif(Direction == 2):
			GPIO.output(direction,GPIO.LOW)
		else:
			raise Exception("number has to be between 1 and 2 ")
		for i in range(int(steps)):
			GPIO.output(step,GPIO.LOW)
			time.sleep(1/StepsPerSec)
			GPIO.output(step,GPIO.HIGH)
			time.sleep(1/StepsPerSec)

	elif(Motor == 2):
		if(Direction == 1):
			GPIO.output(dir2,GPIO.HIGH)
		elif(Direction == 2):
			GPIO.output(dir2,GPIO.LOW)
		else:
			raise Exception("number has to be between 1 and 2 ")
		for i in range(int(steps)):
			GPIO.output(step2,GPIO.LOW)
			time.sleep(1/StepsPerSec)
			GPIO.output(step2,GPIO.HIGH)
			time.sleep(1/StepsPerSec)
	else:
		raise Exception("i only got 2 motors yo ")
	disable(1)


