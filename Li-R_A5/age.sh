#!/bin/bash

age=$1

if [ $age -lt 13 ]; then
	echo "You are a child"
elif [ $age -lt 20 ]; then
	echo "You are a teen"
elif [ $age -lt 65 ]; then
	echo "You are an adult"
else 
	echo "You are an elderly"
fi
