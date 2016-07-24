_author_ = 'mariag'

import re

def toCamelCase(line):
    print re.sub('_',"",re.sub('_\w',lambda m: m.group(0).upper() , line))


def toUnderscore(line):
    print re.sub('[A-Z]', lambda m: '_'+str(m.group(0).lower()),line)
    
print 'toCamelCase'
while True:
    text = raw_input()
    if text == "":
        break
    toCamelCase(text)

print 'toUnderscore'
while True:
    text = raw_input()
    if text == "":
        break
    toUnderscore(text)
