#!/bin/bash

# example usage: init_script.sh 8
# to create 8 nodes

echo Creating $1 instances.

counter=1
while [ $counter -le $1 ]
do
	((counter++))
	# if necessary, change "gnome-terminal" to your own terminal
	gnome-terminal --geometry 50x25 -e "python3 nodeCode.py $1"
done
