import hashlib



"""

Given a file name as string, and the number of nodes,

determines which node that file should be sent to.

Returns an integer from 0 to (number of nodes - 1)

"""

def get_node(file_name, num_nodes):

	m = hashlib.md5()

	m.update(file_name.encode())

	hash_int = int.from_bytes(m.digest(), byteorder='little')

	return hash_int % num_nodes