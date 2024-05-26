#first test of stepping 
#hope i won't fry anything
# STEP PIN -  15
# DIR PIN - 14
# MS1- 8
# MS2 - 25
# MS3 - 24
import atexit
from gpiozero import LED
import os 
from time import sleep
os.system("raspi-gpio set 21 dl") 
step = LED(15)
dir = LED(18)
ms1 = LED(8)
ms2 = LED(25)
ms3 = LED(24)
def shift(x):
	if x == 1:
		#full step 
		ms1.off()
		ms2.off()
		ms3.off()
	if x == 2:
		#half step
		ms1.on()
		ms2.off()
		ms3.off()
	if x == 3:
		#quarter test
		ms1.off()
		ms2.on()
		ms3.off()
	if x == 4:
		#eighth step 
		ms1.on()
		ms2.on()
		ms3.off()
	if x == 5:
		#sixteenth step 
		ms1.on()
		ms2.on()
		ms3.on()
dir.on()
shift(1)
def exit_handler():
	print("lol")
	os.system("raspi-gpio set 21 dh")


try:
	while True:
		sleep(0.01)
		step.on()
		sleep(0.01)
		step.off()
except:
	exit_handler()
