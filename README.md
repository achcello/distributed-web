# Chord Development
## Things that work:
1. Finger tables are correctly generated upon node creation.
2. Each node uses the same code to operate and can act as both a server and a client at the same time.
3. The basic structure is there for the future.
## Things to improve:
1. IDs need to be hashed.
2. IDs, addresses, ports, et cetera need to be generalized, not hard-coded.
3. The handoff between nodes searching for nodes searching for nodes doesn't really work yet. (It's really just the transmission of the address that needs to be resolved.)
4. There is an infinite loop which prohibits nodes from contacting nodes indirectly.
