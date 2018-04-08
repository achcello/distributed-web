#!/bin/bash

echo Creating $1 instances.

counter=1
while [ $counter -le $1 ]
do
	#echo here
	((counter++))
	gnome-terminal --geometry 50x25 -e "python3 nodeCode.py $1"
done
