#!/usr/bin/env python3
# coding=utf-8
# You need to input one argument for this application - text
# The program will detect if the text are characters, bopomofo or pinyin
# then it will output a text with Tradtional + Simplified + Bopomofo + Pinyin
# It will be in the console and your clipboard
# Credit: pdyq

from dragonmapper import hanzi, transcriptions
from hanziconv import HanziConv
import clipboard
import re

text = ""

# Get only Chinese characters
def pickUp(i):
    j = ""
    for n in re.findall(r"[\u4e00-\u9fff]+", i):
        j = j + n
    return j


# Get the text
inputr = clipboard.paste()

text = pickUp(inputr)


# main function
def main(s):
    rule = hanzi.identify(s)
    trad = ""
    simp = ""
    bpmf = ""
    py = ""
    match rule:
        case 0:
            print("GIVE UP")
        case 3:
            trad = s
            simp = 0
            bpmf = hanzi.to_zhuyin(s)
            py = hanzi.to_pinyin(s)
        case _:
            trad = HanziConv.toTraditional(s)
            simp = HanziConv.toSimplified(s)
            bpmf = hanzi.to_zhuyin(HanziConv.toTraditional(s))
            py = hanzi.to_pinyin(HanziConv.toTraditional(s))
    if simp:
        clipboard.copy(trad + "(" + simp + ") " + bpmf + " " + py)
    else:
        clipboard.copy(trad + " " + bpmf + " " + py)


main(text)
