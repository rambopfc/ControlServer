#The goal of this program is to have a server/service on a remote system that will provide control of volume from a client over TCP
#This code is taken from a guide at http://www.binarytides.com/python-socket-programming-tutorial/ and modified to fit my needs
#to do the actual volume control I am using http://www.nirsoft.net/utils/nircmd.html 64bit

import socket
import sys
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


while 1:
    conn, addr = s.accept()
    data = conn.recv(9999)
    subprocess.Popen("nircmd.exe mutesysvolume 1")
    conn.close()
    if not data:
        break
    


conn.close()
s.close()
