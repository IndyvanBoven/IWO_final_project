#!/bin/python3
# Author: I. van Boven

import sys
import re

def main(argv):
    north = ['(friesland)', '(groningen)', '(drenthe)']
    provinces = ['(friesland)', '(groningen)', '(drenthe)', '(zeeland)', '(noord-brabant)', '(limburg)']
    not_north_provinces = ['(noord-holland)', '(zuid-holland)', '(utrecht)', '(flevoland)', '(gelderland)', '(overijssel)', '(zeeland)', '(noord-brabant)', '(limburg)']
    south = ['(zeeland)', '(noord-brabant)', '(limburg)']
    not_south_provinces = ['(noord-holland)', '(zuid-holland)', '(utrecht)', '(flevoland)', '(gelderland)', '(overijssel)', '(friesland)', '(groningen)', '(drenthe)']
    double_list = []
    file = argv[1]
    with open(file, 'r') as inp:
        text = inp.read()
        text = re.split('\n', text)
        for lines in text:
            line = lines.lower()           
            for word in north:
                for i in not_north_provinces:
                    if word in line and i in line:
                        double_list.append(line)
                        
            for province in south:
                for place in not_south_provinces:
                    if province in line and place in line:
                        double_list.append(line)
                        
        for places in double_list:
            print(places)


if __name__ == "__main__":
    main(sys.argv)