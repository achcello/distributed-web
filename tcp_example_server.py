import socket
import sys

# Create a tcp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(8)
    datastr = data.decode()

    if len(data) > 0:
        ackmsg = "Good job, %s" % datastr
        sock.sendto(ackmsg.encode('utf-8'), address)
        print(ackmsg)
