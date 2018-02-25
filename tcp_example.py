import socket
import sys

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address
#addr = input("Enter the target IP address: ")
#port = int(input("Enter the target port: "))
server_address = ('10.195.61.229', 10000)

# create the TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
sock.connect(server_address)

# get some data to send and send it
# message = "Something hard-coded bc input wasn't working for some reason . . . I guess this is one way to flow text."
message = raw_input("Type something idk: ")
sock.sendall(message)

# make sure the entire message gets sent and received
# because it's being done by character
amount_received = 0
amount_expected = len(message)
message = ""
while amount_received < amount_expected:
	data = sock.recv(16)
	amount_received += len(data)
	message += data
	print("In progress: ", data)
	print(amount_received)
sock.close()
print(message)