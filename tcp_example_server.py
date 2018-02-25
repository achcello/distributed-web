import socket
import sys

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt to bind the socket to the port
# Make accessible to local network
server_address = ('0.0.0.0', 10000)
connected = False
while not connected:
	try:
		sock.bind(server_address)
		sock.listen(1)
		connected = True
	except:
		pass

# print a connection message if it was successful
print('starting up on %s port %s' % server_address)

# Wait for connection from a client
connection, client_address = sock.accept()

#Receive data from client, 16 characters at a time
message = ""
terminator = 0
while terminator < 15:
    data = connection.recv(16)
    connection.sendall(data)
    #print(data) # I just want to see what this is
    message += data
    terminator +=1

# close the connection
connection.close()

print(message)