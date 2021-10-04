#! /usr/bin/env bash

GREETINGS=("Good Morning" "Good Afternoon")


for GREET in "${GREETINGS[*]}"; do
   echo "GREET: $GREET"
done

for GREET in "${GREETINGS[@]}"; do
   echo "GREET: $GREET"
done
