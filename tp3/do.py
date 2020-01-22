#!/usr/bin/python3
"""
"""

import re
import subprocess
import sys
from getopt import getopt
import fileinput
from collections import Counter


def main(filename):
    type = "tagger"
    lang = "pt"
    return subprocess.run([f"linguakit {type} {lang} {filename}"],shell=True,capture_output=True)
    
main("~/Code/git_projects/ipln-1920-i/data/Os_Maias.txt")
