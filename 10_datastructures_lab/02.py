"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""

_author_ = 'mariag'

import sys
from collections import Counter

file_words = 'words.txt'
wordsDic = {}

#load key=sorted word|value=original word to dictionary
with open(file_words, 'r') as f_words:
    for word in f_words:
        stripWord = word.rstrip('\n')
        sortedWord = ''.join(sorted(stripWord))
        if sortedWord in wordsDic:
            wordsDic[sortedWord].append(stripWord)
        else:
            wordsDic[sortedWord] = [stripWord]

for k,v in wordsDic.items():
    print ""
    for i in v:
        sys.stdout.write(i+"\t")