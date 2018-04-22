#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import sys
      # Create a socket object
host = '127.0.0.1'
port = 10001             # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))        # Bind to the port

#s.listen(5)                 # Now wait for client connection.
s.connect((host, 5005))
#c, addr = s.accept()     # Establish connection with client.
#print ('Got connection from',addr)
#message = 'a'.encode()
#s.send(message)
response = s.recv(1024)
response = response.decode()
print (response)

s.close()