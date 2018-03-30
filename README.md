# Chord Development

## Things that work:
1. Finger tables are correctly generated upon node creation.
2. Each node uses the same code to operate and can act as both a server and a client at the same time.
3. A server is able to hand off a request for a server not in its finger table to the correct address.
4. The basic structure is there for the future.

## Things to improve:
1. IDs need to be hashed.
2. IDs, addresses, ports, et cetera need to be generalized, not hard-coded (to an extent).
3. Once the number of nodes, $n$, is generalized, we can test the system with an arbitrary (maybe slightly less than arbitrary) number of nodes.
4. Eventually, we want to transfer more data through this system than just simple pings.