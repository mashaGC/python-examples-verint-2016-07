_author_ = 'mariag'

import sys
import os

file = sys.argv[1]

print file

try:
    lines = sum(1 for line in open(file))
    print "Amount of lines in {} is {}".format(file, lines)
except IOError as e:
    print "Sorry, file {} not found".format(file)