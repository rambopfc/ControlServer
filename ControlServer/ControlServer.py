#The goal of this program is to have a server/service on a remote system that will provide control of volume from a client over TCP
#This code is taken from a guide at http://www.binarytides.com/python-socket-programming-tutorial/ and modified to fit my needs
#to do the actual volume control I am using http://www.nirsoft.net/utils/nircmd.html 64bit

import socket
import sys
#from thread import *
import _thread
import threading
import subprocess
import struct

HOST = '127.0.0.1'
PORT = 8888
data = struct.Struct('>i')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.bind((HOST, PORT))
except socket.error as e:
	print('Bind failed. Error Code : ' + str(e))
	sys.exit()

s.listen(2)

#Function for handling connections. This will be used to create threads
#def clientthread(conn):
#   while True:
#        data = conn.recv(1024)
#        print(str(data))
#        if not data:
#            break
#        elif str(data) == "mute":
#            subprocess.Popen("nircmd.exe mutesysvolume 1")
#        elif str(data) == "low":
#            subprocess.Popen("nircmd.exe changesysvolume -2000")
#
#    conn.close()

while 1:
    conn, addr = s.accept()
    data = conn.recv(9999)
    subprocess.Popen("nircmd.exe mutesysvolume 1")
    conn.close()
    if not data:
        break
    

    #wait to accept a connection - blocking call
#	conn, addr = s.accept()
#	data = conn.recv(9999)
#    socket_file = conn.makefile()


#    print(value)

conn.close()
s.close()
#threading.Thread(target=clientthread, args=(conn)).start()

#        elif str(data) == "mute":
#            subprocess.Popen("nircmd.exe mutesysvolume 1")
#        elif str(data) == "low":
#            subprocess.Popen("nircmd.exe changesysvolume -2000")