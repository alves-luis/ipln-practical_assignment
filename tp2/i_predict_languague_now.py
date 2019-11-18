#!/usr/bin/python3
"""
I Predict Language Now (IPLN) - detects the language of a txt file, and improves
our cool db
"""

import re
import subprocess
import sys
from getopt import getopt
import fileinput
from collections import Counter
import shelve
#import counter

def find_lang(texto, filename, language_counter):
    num_w = 0
    d = shelve.open( filename )  # open -- file may get suffix added by low-level
    for word in texto.split(" "): # run through every word of the text
        num_w += 1
        if word in d: # check if the word exists in the dictonaries
            for language in d[word]: # run through the list of languages
                language_counter[language] += 1
    d.close()
    return num_w

# returns the percentage of the winner and closest loser language vs number of words
def print_stats(language_counter, num_words):
    top_2 = language_counter.most_common(2)
    percentage_of_winner_lang = top_2[0][1] / num_words * 100
    percentage_of_loser_lang = top_2[1][1] / num_words * 100
    print(f"I believe this text is in {top_2[0][0]}! I'm {percentage_of_winner_lang}% sure!")
    if percentage_of_loser_lang > 50:
        print(f"However, it was a close call! {top_2[1][0]} seems like a close fit, with {percentage_of_loser_lang}% of matching words!")
    return percentage_of_winner_lang, percentage_of_loser_lang

def main():
    opts, resto = getopt(sys.argv[1:],"")
    dop = dict(opts)

    cnt = Counter() # counter by language

    print(resto)
    texto = ""

    # Reads file
    for line in fileinput.input(resto[1]):
        texto += line

    num_words = find_lang(texto,resto[0], cnt)
    percent_win, percent_los = print_stats(cnt, num_words)
    # if percentage is something something, add to dictionary
    # TODO

main()
