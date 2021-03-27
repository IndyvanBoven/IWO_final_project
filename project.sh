#!/bin/bash
#Indy van Boven



path=drenthe_py.py
FILE=$1
FILE2=$2

#for north
grep '^[[:alpha:]]' $FILE | python3 $path 

#for south
grep '^[[:alpha:]]' $FILE2 | python3 $path