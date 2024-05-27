import socket
timeout = False 
def setTimeout(x):
	global timeout
	timeout = x
def sendMessage(message):
	global timeout
	msgFromClient       = message
	bytesToSend         = str.encode(msgFromClient)
	serverAddressPort   = ("192.168.68.72", 20001)
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



 