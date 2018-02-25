import socket
import sys

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address
addr = input("Enter the target IP address: ")
port = int(input("Enter the target port: "))
server_address = (addr, port)

# Message to send
message = bytes(input("Enter your NetID: "), "utf-8")

try:
    # Send data
    sent = sock.sendto(message, server_address)

    # Receive response
    data, server = sock.recvfrom(4096)
    print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()
