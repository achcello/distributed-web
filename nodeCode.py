import socket
import sys
import time
import keyboard
import multiprocessing

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
	print('Starting up on %s port %s' % server_address)
	print('(Waiting for a request in background . . . )\n')

	while True:
		# Wait for connection from a client or input from user

		client_ip, client_port = serverSock.accept()

		# receive node search request from client
		data = client_ip.recv(1)
		requestedID = data.decode('utf-8')
		print("Searching for node", requestedID) # D E B U G    

		if requestedID == node_id:
			response = "found".encode('utf-8')
		else:
			#print('wow much lookup')
			# look up the request in the finger table
			distToTarget = 3 # max is n-1 which is hardcoded for now
			closestID = ''
			for ids in fingerTable.keys():
				distToTarget = int(requestedID) - int(ids)
				closestID = ids
				if distToTarget <= 0:
					break
			response = ('localhost' + ' 1000' + closestID).encode('utf-8')

		print('sending', response)
		client_ip.sendall(response)
		client_ip.close()
		print('Resetting listener . . .')
		print('Request a node:')

def inputNode():
	"""
	Get the node to be requested.
	"""

	#print('#entering inputNode()')
	# get the node request number
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
		distToTarget = 3 # max is n-1 which is hardcoded for now
		server_address = ('empty', 0)
		for ids in fingerTable.keys():
			distToTarget = int(nodeSearch) - int(ids)
			server_address = fingerTable[ids]
			if distToTarget <= 0:
				break

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
		print('Server responded:', response)
		responseIP = ''
		try:
			responseIP = int( response.split(' ')[0] )
			responsePort = response.split(' ')[1]
		except:
			pass
		
		if response == "found":
			print(response)
			print('Node %s found!' % nodeSearch)
			clientSock.close()
			break
		elif responseIP != '':
			print('Not found yet; contacting', response)
			fingerTable[ responsePort[-1] ] = (responseIP, responsePort)
			searchNode(nodeSearch)


if __name__ == '__main__':
	"""
	This main method creates the server socket (which shouldn't change address/port)
	and generates the finger table. It then starts the server process as a daemon
	and runs it in the background as the client code is run.
	"""

	# Create a TCP socket
	serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Attempt to bind the socket to the port
	# Make accessible to local network
	# ask for the IP and port as user inputs, will be automated in the future
	node_ip = 'localhost' # input('Input the node IP address: ')
	node_id = input("Input the node's number (for now, in [0,3]): ")
	node_port_base = 10000
	node_port = 10000 + int(node_id)
	wrappedID1 = (int(node_id) + 1)%4
	wrappedID2 = (int(node_id) + 2)%4

	fingerTable = {}
	fingerTable[ str(wrappedID1) ] = (node_ip, (node_port_base + wrappedID1))
	fingerTable[ str((int(node_id) + 2)%4) ] = (node_ip, (node_port_base + wrappedID2))
	print('Finger table:\n', fingerTable)

	node_port = 10000 + int(node_id)

	# set up the request listener as a daemon in the background
	listener = multiprocessing.Process(name='serverNode', target=serverNode)
	listener.daemon = True
	listener.start()
	time.sleep(3)
	print('Listener daemon started')

	while True:
		searchNode(inputNode())