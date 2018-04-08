#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import sys
s = socket.socket()         # Create a socket object
host = '127.0.0.1' # Get local machine name
port = 5010             # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

c, addr = s.accept()     # Establish connection with client.
print ('Got connection from',addr)
message = 'a'.encode()
c.send(message)
response = c.recv(1024)
response = response.decode()
print (response)

#c.close()