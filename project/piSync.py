import os
import  sys
try:
	myfile = open("./pyip.txt")
	ip = myfile.readline().rstrip()
except:
	print("cannot find pyip file")
	exit()
condition = sys.argv[1]
try:
	if(condition  == "upload"):
		mystr = ("scp -r -p /home/diosz/Desktop/project/ pi@"+str(ip)+":/home/pi/")
		os.system(mystr)
	elif (condition == "download"):
		a = input("Warning!The following action will OVERWRITE local files. Do you wish to proceed?")
		if(a!="yes" or a!="y" or a!= "Yes" or a!="YES"):
			exit()
		mystr = ("scp -r -p pi@"+str(ip)+":/home/pi/project /home/diosz/Desktop/")
		os.system(mystr)
except:
	print("usage: python3 piSync.py upload \n python3 piSync.py download")
