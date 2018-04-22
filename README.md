# Distributed Web

## Setup

### Dependencies

* This project is developed using Python 3.6.
* Python dependencies can be found in `requirements.txt` and can be installed using `pip install -r requirements.txt`.

### Chord Nodes

* The node generation script, `init_script.sh`, assumes the availability of the gnome-terminal. Make sure to change this to your respective terminal.

## Usage

### Setup for the Chord Network

1. Use `init_script.sh` to generate the desired number of nodes. Include this number as a command line argument. These examples will use eight nodes.
```bash
$ ./init_script.sh 8
Creating 8 instances.
```
1.5. To create one node manually, use:
```bash
$ python3 nodeCode.py 8
```
2. Assign each node an ID in the given range.

### Divided files to store into Nodes

1. Using 'split.py' allows a dictionary to be split equally by keys in order to distribute the webpages on multiple servers.

2. Using 'join.py' rejoins the split code together based on the keys made in the dictionaries.

### Run Flask Server

1. Open 'filePost.py' and specify host and port in main method. Run in terminal:
'''
$ python3 filePost.py
'''
2.1. To upload file, in the broswer run:
http://host:port/post

## Features

* Finger tables of node addresses are generated upon node creation.
* Each node uses the same code to operate and can act as both a server and a client at the same time; this provides verisimilitude between nodes which is an important part of decentralization.
* A server is able to hand off a request for a server not in its finger table to the correct address or to a server which is closer to the correct address.

## Development

* IDs need to be hashed.
* IDs, addresses, ports, et cetera need to be generalized, not hard-coded (to an extent).
* Once the number of nodes, $n$, is generalized, we can test the system with an arbitrary (maybe slightly less than arbitrary) number of nodes.
* Eventually, we want to transfer more data through this system than just simple pings.
