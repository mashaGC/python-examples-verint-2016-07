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

#load key=word|value=letter counter to dictionary
with open(file_words, 'r') as f_words:
    for word in f_words:
        wordsDic[word.rstrip('\n')] = Counter(word.rstrip('\n'))

#print wordsDic
delList =[]
while len(wordsDic)>0:
    for i in delList:
        del wordsDic[i]
    delList = []
    print("")
    word = wordsDic.keys()[0]
    counter_i = wordsDic.get(word)
    sys.stdout.write(word+" ")
    del wordsDic[word]
    for word_i in wordsDic:
        if  counter_i == wordsDic.get(word_i):
            sys.stdout.write(word_i+" ")
            delList.append(word_i)