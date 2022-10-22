import os
import socket
import threading
import time
#AF_INET -> TO USE ipv4 , SOCK_STREAM->we are using TCP/IP protocol stack for communication with client.
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
host='127.0.0.1';
port=6006;
s.connect((host, port));

def fromServer():
	#receive message from server
	global s, host, port,msg
	msg=s.recv(1024);
	try:
		while msg:
			seconds = time.time()
			local_time = time.ctime(seconds)
			print("Local time:", local_time)
			print(msg.decode());
			msg=s.recv(1024);
	except KeyboardInterrupt:
		print("Keyboard interrupt exception caught.Exiting ...")
		s.close()
		
def client():
	#send message to server
	global s, host, port, msg
	try:
		while True:
			text = input("");
			s.send(text.encode());
	except KeyboardInterrupt:
		print("Keyboard interrupt exception caught.Exiting ...")
		s.close()

#create threads for two functions
thread1 = threading.Thread(target=fromServer)
thread2 = threading.Thread(target=client)

#start threads for two functions
thread1.start()
thread2.start()
