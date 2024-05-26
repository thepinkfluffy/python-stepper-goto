import RPi.GPIO as GPIO
import time

step = 16
dir = 21
en = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(step,GPIO.OUT)
GPIO.setup(dir,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(en,GPIO.LOW)
for x in range(100):
	GPIO.output(dir, GPIO.LOW)
	GPIO.output(step,GPIO.LOW)
	time.sleep(0.01)
	GPIO.output(step,GPIO.HIGH)
GPIO.output(en,GPIO.HIGH)
#GPIO.cleanup()

