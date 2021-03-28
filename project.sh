#!/bin/bash
#Indy van Boven

path=final_project.py
FILE=$1
FILE2=$2

#for north
grep '^[[:alpha:]]' $FILE | python3 $path 

#for south
grep '^[[:alpha:]]' $FILE2 | python3 $path
