#!/usr/local/bin/python3
"""
Ngrams - Calculate ngrams frequency
"""

import re
import subprocess
import sys
from getopt import getopt
import fileinput
from collections import Counter
import shelve
#import counter

cnt = Counter() # counter

def find_la(texto, filename):
    d = shelve.open( filename )  # open -- file may get suffix added by low-level
    for w in texto.split(" "): # run through every word of the text
        if w in d: # check if the word exists in the dictonaries
            for i in d[w]: # run through the list of languages
                cnt[i] += 1
    d.close()

def main():
    opts, resto = getopt(sys.argv[1:],"")
    dop = dict(opts)

    print(resto)
    texto = ""

    # Reads file
    for line in fileinput.input(resto[1]):
        texto += line

    find_la(texto,resto[0])
    print(cnt.most_common(1))


main()
