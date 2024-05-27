import socket
def sendMessage(message):
	msgFromClient       = message
	bytesToSend         = str.encode(msgFromClient)
	serverAddressPort   = ("192.168.68.71", 20001)
	bufferSize          = 1024
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	UDPClientSocket.settimeout(2)
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	try:
		msgFromServer = UDPClientSocket.recvfrom(bufferSize)
		return True
	except socket.timeout as s:
		return False



 