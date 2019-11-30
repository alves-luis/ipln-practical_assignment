#!/usr/local/bin/python3

"""
I Predict Language Now (IPLN) - detects the language of a txt file, and improves
our cool db
"""

import re
import sys
from getopt import getopt
import fileinput
from collections import Counter
import shelve

def find_lang(texto, dic, language_counter):
    num_w = 0
    for word in [i for i in re.split(r'[\s\t\n,.?!]',texto) if i]: # run through every word of the text
        num_w += 1
        if word in dic: # check if the word exists in the dictionaries
            for language in dic[word]: # run through the list of languages
                language_counter[language] += 1
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


# if option -A
def add_text_to_dict(d,texto,percent_win,language_to_add, resto):
    for e in range(len(resto)):
        if resto[e] == '-A':
            percentage_to_add = resto[e+1]

    if percent_win > int(percentage_to_add):
        for word in re.split(r'[\s\t\n,.?!]',texto):
            # Check if the word exists in the dictionary
            if word in d:
                # Check if the word in the dictionary has the language_to_add
                if language_to_add not in d[word]:
                    var = d[word];
                    var.append( language_to_add )
                    d[word] = var
                else:
                    # If word doesn't exist in the dictionary add it
                    d[word] = [language_to_add]


def main():
    opts, resto = getopt(sys.argv[1:],"A")
    dop = dict(opts)

    cnt = Counter() # counter by language

    texto = ""
    # Reads file
    for line in fileinput.input(resto[1]):
        texto += line

    d = shelve.open( resto[0]) # open -- file may get suffix added by low-level

    num_words = find_lang(texto, d , cnt)
    percent_win, percent_los = print_stats(cnt, num_words)

    language_to_add = cnt.most_common(1)[0][0]

    if '-A' in resto:
        add_text_to_dict(d,texto,percent_win,language_to_add,resto)

    d.close()

main()
