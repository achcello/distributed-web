import socket
import sys
import time
import subprocess
import multiprocessing
from math import log

def serverNode():
	p = multiprocessing.current_process()
	server_address = (node_ip, node_port)
	connected = False
	while not connected:
		try:
			serverSock.bind(server_address)
			serverSock.listen(1)
			connected = True
		except:
			print('Not yet connected . . . ')
			time.sleep(3)

	# print a connection message if it was successful
	print('\nListening on %s port %s' % server_address)
	print('(Waiting for a request in background . . . )\n')

	while True:
		# Wait for connection from a client or input from user

		client_ip, client_port = serverSock.accept()

		# receive node search request from client
		data = client_ip.recv(1) #retrieve data from split.py
		#https://stackoverflow.com/questions/13698352/storing-and-accessing-node-attributes-python-networkx 
		requestedID = data.decode('utf-8')
		print("Searching for node", requestedID) # D E B U G    

		if requestedID == node_id:
			response = "found".encode('utf-8')
		else:
			print('redirecting . . . ')
			# look up the request in the finger table
			distToTarget = n - 1 # max is n-1 which is hardcoded for now
			closestID = ''
			print("truth:", requestedID in fingerTable.keys())
			if requestedID in fingerTable.keys():
				response = ('localhost' + ' 1000' + requestedID).encode('utf-8')
			else:
				minPosDist = 0
				for ids in fingerTable.keys():
					distToTarget = int(requestedID) - int(ids)
					if distToTarget > 0 and distToTarget < int(requestedID) - int(minPosDist):
						minPosDist = ids
				closestID = minPosDist
				response = ('localhost' + ' 1000' + closestID).encode('utf-8')

		print('sending', response)
		client_ip.sendall(response)
		client_ip.close()
		print('Resetting listener . . .')
		print('\nRequest a node:')

def inputNode():
	"""
	Get the node to be requested.
	"""

	#print('#entering inputNode()')
	# get the node request number
	nodeSearch = input("\nRequest a node:\n")
	while (not nodeSearch.isdigit or nodeSearch == "" or nodeSearch == str(node_id) or int(nodeSearch) >= n):
		print("Please enter a digit in (0,n).")
		nodeSearch = input("Request a node:\n")
	return nodeSearch

def searchNode(nodeSearch):
	"""
	Search for a requested node. If it is not found, the server will search and again
	and so on.
	"""

	#print('#entering searchNode()')
	while True:

		# look up the request in the finger table
		distToTarget = n - 1 # max is n-1
		server_address = ('empty', 0)
		if nodeSearch in fingerTable.keys():
			server_address = fingerTable[nodeSearch]
		else:
			for ids in fingerTable.keys():
				distToTarget = int(nodeSearch) - int(ids)
				if distToTarget < 0:
					break
				server_address = fingerTable[ids]

		# create the TCP socket
		clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# connect to the server
		print('Requesting node', nodeSearch)
		#print('Server address:', server_address)
		try:
			clientSock.connect(server_address)
		except:
			print('Connection failed')
			break
		clientSock.sendall(nodeSearch.encode('utf-8'))
		response = clientSock.recv(48).decode('utf-8')
		response = response.strip()
		print('Server responded:', response)

		if response == "found":
			print('Node %s found!' % nodeSearch)
			clientSock.close()
			break

		try:
			responseIP = response.split(" ")[0]
			responsePort = int( response.split(" ")[1] )
		except:
			print("splitting the response into IP and port didn't work")
			print("things are going to fail now gg")
		
		print('Not found yet; contacting', response)
		fingerTable[ str(responsePort % 10) ] = (responseIP, responsePort)
		print( fingerTable )
		searchNode(nodeSearch)


if __name__ == '__main__':
	"""
	This main method creates the server socket (which shouldn't change address/port)
	and generates the finger table. It then starts the server process as a daemon
	and runs it in the background as the client code is run.
	"""

	n = int( sys.argv[1] ) # n = number of nodes

	# Create a TCP socket
	serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Attempt to bind the socket to the port
	# Make accessible to local network
	# ask for the IP and port as user inputs, will be automated in the future
	node_ip = 'localhost' # input('Input the node IP address: ')
	node_id = input("Input the node's number (in [0," + str(n-1) + "]): ")
	node_port_base = 10000
	node_port = 10000 + int(node_id)
	wrappedIDs = []
	addID = 1
	for _ in range( int( round( log(n, 2) ) ) ):
		wrappedIDs.append((int(node_id) + addID)%n)
		addID *= 2

	# Generate the appropriate finger table
	fingerTable = {}
	for newFinger in wrappedIDs:	
		fingerTable[ str( newFinger ) ] = (node_ip, (node_port_base + newFinger))
	print('\nFinger table:')
	for entry in fingerTable.keys():
		print( entry,":", fingerTable[entry])

	node_port = 10000 + int(node_id)

	# set up the request listener as a daemon in the background
	listener = multiprocessing.Process(name='serverNode', target=serverNode)
	listener.daemon = True
	listener.start()
	time.sleep(2)
	print('Listener daemon started')

	while True:
		searchNode(inputNode())
