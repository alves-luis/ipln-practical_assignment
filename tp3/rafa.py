#!/usr/bin/python3

import re

def getPattern(padrao):
    result = ""
    for p in padrao.split(" "):
        result += rf"(\w+) \w+ {p}\n"
    return result

def match(txt,padrao):
    solution = []
    pattern = getPattern(padrao)
    for res in re.findall(pattern,txt):
        solution.append(" ".join(res))
    return solution
