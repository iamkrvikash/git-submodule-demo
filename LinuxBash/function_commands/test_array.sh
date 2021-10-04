#! /usr/bin/env bash

ARRAY=(Apple Orange Mango)

echo ${ARRAY[0]}

echo "At index 1 : ${ARRAY[1]} "

ARRAY[3]="Banana"

echo ${ARRAY[2]} ${ARRAY[3]}

