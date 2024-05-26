import socket
from motor_control import move,enable,disable
import RPi.GPIO as GPIO
localIP = "192.168.68.71"
localPort   =  20001
bufferSize  = 1024
msgFromServer       = "itt a kezem"
bytesToSend         = str.encode(msgFromServer)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
UDPServerSocket.setblocking(0)
print("UDP server up and listening")
clientMsg=""
stepsPerSec = 800
step = 1
degrees = 40
while(True):
	try:
		bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
		message = bytesAddressPair[0]
		address = bytesAddressPair[1]
		clientMsg = str(message)[2]
		print("socket received: "+clientMsg)
	except:
		pass
	if(clientMsg =="1" or clientMsg =="2"):
		if(degrees>0):
			direction = 1
		if (degrees<0):
			direction = 2
		if(clientMsg == "1"):
			move(direction,step,1,stepsPerSec,degrees)
			pass
			#print("moving up")
		elif(clientMsg == "2"):
			move(direction,step,2,stepsPerSec,degrees)
			pass
			#print("moving down")
	if(clientMsg=="5"):
		disable(1)
	#       print("stopped")
	if(clientMsg=="6"):
		stepsPerSec = 100
	if(clientMsg=="7"):
		stepsPerSec = 200
	if(clientMsg=="8"):
		stepsPerSec = 300
	if(clientMsg=="9"):
		stepsPerSec =500
	if(clientMsg=="a"):
		stepsPerSec = 800

	if(clientMsg=="b"):
		step = 1
	if(clientMsg=="c"):
		step = 2
	if(clientMsg=="d"):
		step = 3
	if(clientMsg=="e"):
		step = 4
	if(clientMsg=="0"):
		try:
			UDPServerSocket.sendto(bytesToSend ,address)
		except:
			pass
	if(clientMsg[:3]=="deg"):
		degrees = float(clientMsg[3:])
		print("received new degrees "+str(degrees))
