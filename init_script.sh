#!/bin/bash

echo Creating $1 instances.

counter=0
while [ $counter -le $1 ]
do
	#echo here
	((counter++))
	gnome-terminal --geometry 50x25 --window-with-profile=sarte -e "python3 nodeCode.py $1"
done