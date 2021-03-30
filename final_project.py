#!/bin/python3
# Author: I. van Boven

import sys
import re


def dubbel(argv):
    double_places = []
    file2 = 'double_places_nl.txt'
    with open(file2, 'r') as infile:
        words = infile.read()
        words = words.lower()
        dubbel_list = re.split('\n', words)
        for locations in dubbel_list:
            location = re.sub(r'([a-z]) \(', r'\1\t(', locations) #Places tab between first word and second of each line
            place = re.split('\t', location)
            double_places.append(place[0])
        double_places.append('lombok') #double place
        double_places.append('park') #double place
        double_locations = set(double_places)

    return double_locations

   
def create_list(argv):
    file_north = 'north.txt'
    file_south = 'south.txt'
    with open(file_north, 'r') as inp_north:
        text = inp_north.read()
        text = text.lower()
        places_n = re.split(' \t|\n', text)
        north_list = set(places_n)
        
    with open(file_south, 'r') as inp_south:
        text2 = inp_south.read()
        text2 = text2.lower()
        places_s = re.split(' \t|\n', text2)
        places_s = [re.sub('\?', '', i) for i in places_s] #Replaces questionmarks
        south_list = set(places_s)
    
    return north_list, south_list


def specific_cases(split_line):
    replace_tabs = re.sub(r'(de|den|ter|ten|\'t)\t', r'\1 ', split_line)        #Removes tabs in a location (e.g.Den Helder)
    remove_tabs = re.sub('\t-\t?', '-', replace_tabs)                           #Example: oost  -   fryslan becomes oost-fryslan
    comma_tabs = re.sub('\'\tt\t', '\'t ', remove_tabs)                         #Replaces tabs between ' and t, 't Loo Oldebroek
    add_punct = re.sub('noord\toost', 'noord-oost', comma_tabs)                 #Adds -, noord oost becomes noord-oost
    add_punct_east = re.sub(r'([a-z])\toost^-', r'\1-oost', add_punct)          
    add_punct_north = re.sub(r'([a-z])\tnoord^-', r'\1-noord', add_punct_east)  #Same ^, but avoids hoorn-noord-holland
    punct_north = re.sub(r'noord\t([a-z])', r'noord-\1', add_punct_north)       #Adds -, e.g. noord holland, becomes noord-holland
    punct_east = re.sub(r'oost\t([a-z])', r'oost-\1', punct_north)              #Adds -, e.g. Oost Gelderland, becomes Oost-Gelderland
    special_case = re.sub('aan\thet\tstrand', 'aan het strand', punct_east)    
    special_cases = re.sub('loon\top\tzand', 'loon op zand', special_case)      
    spec_case = re.sub('nes\ta', 'nes a', special_cases)                        
    split_locations = spec_case.split('\t')
    
    return split_locations


def main(argv):
    tweets_south = []
    tweets_north = []
    count_n = 0
    count_s = 0
    total_count = 0
    north_list, south_list = create_list(argv)
    double_locations = dubbel(argv)
    for lines in sys.stdin:
        total_count +=1
        line = lines.lower()
        line = re.split('\t|\n', line)
        split_line = re.sub(', |,| |/', '\t', line[0])
        split_locations = specific_cases(split_line)
        
        for word in split_locations:
            if word in north_list and not word in south_list:
                if not word in double_locations:
                    lines = lines.strip()
                    tweets_north.append(lines)
                    
            elif word in south_list and not word in north_list:
                if not word in double_locations:
                    lines = lines.strip()
                    tweets_south.append(lines)

    tweets_north = set(tweets_north)
    for n_places in tweets_north:
        count_n += 1
        
    tweets_south = set(tweets_south)
    for s_places in tweets_south:
        count_s += 1
        
    print("North: {0}".format(count_n))
    print("South: {0}".format(count_s))
    print("Total number of tweets: {0}".format(total_count))


if __name__ == "__main__":
    main(sys.argv)
