import socket
import os
import time
import threading

#AF_INET -> TO USE ipv4 , SOCK_STREAM->we are using TCP/IP protocol stack for communication with client.
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
host='127.0.0.1';
port=6006;
s.bind((host, port));
s.listen(5);#try to establish connection 5 times before refusing it.
conn, addr = s.accept();
#print(conn)

def toClient():
	#send message to client
	global s, host, port,conn
	try:
		while True:
			text = input("");
			conn.send(text.encode());
	except KeyboardInterrupt:
		print("Keyboard interrupt exception caught.Exiting ...")
		s.close()
		
def server():
	#receive message from client
	global s, host, port
	msg=conn.recv(1024);
	try:
		while msg:
			seconds = time.time()
			local_time = time.ctime(seconds)
			print("Local time:", local_time)
			print(msg.decode());
			msg=conn.recv(1024);
	except KeyboardInterrupt:
		print("Keyboard interrupt exception caught.Exiting ...")
		s.close()
		
#create threads for two functions
thread1 = threading.Thread(target=toClient)
thread2 = threading.Thread(target=server)

#start threads for two functions
thread1.start()
thread2.start()
