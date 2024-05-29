import socket
import sys 
myfile = open("./piip.txt")

timeout = False 
ip = myfile.readline().rstrip()
if(__name__ == "__main__"):
	condition = sys.argv[1]
	if (condition == "ipupdate"):
		ip = sys.argv[2]
		with open("./piip.txt","w") as myfile:
			myfile.write(ip)
	else:
		raise Exception("Unkown arguments")
def setTimeout(x):
	global timeout
	timeout = x
def sendMessage(message):
	global ip
	global timeout
	msgFromClient       = message
	bytesToSend         = str.encode(msgFromClient)
	serverAddressPort   = (ip, 20001)
	bufferSize          = 1024
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	UDPClientSocket.settimeout(3)
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	if(timeout is not True):
		try:
			msgFromServer = UDPClientSocket.recvfrom(bufferSize)
			return True
		except socket.timeout as s:
			return False



 
