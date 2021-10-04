#! /usr/bin/env bash

for((;;));do
	if [ $COUNTER -eq 5 ]; then
		exit
	else
		echo "Current no.is: $(( COUNTER++))"
	fi
done
