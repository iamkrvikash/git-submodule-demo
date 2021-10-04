#! /usr/bin/env bash

FIRST_NAME='John'
LAST_NAME='Doe'

function say_hello(){
	FIRST_NAME=$1           #global scope
	local LAST_NAME=$2      #local scope

	echo "Hello, $FIRST_NAME $LAST_NAME"
}

echo "Before ; First_Name $FIRST_NAME, Last_Name: $LAST_NAME"
say_hello Ross Guy
echo "After ; First_Name $FIRST_NAME, Last_Name: $LAST_NAME"

