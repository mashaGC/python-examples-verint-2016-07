_author_ = 'mariag'

from sys import argv

def isInt(input):
    try: 
        int(input)
        return True
    except ValueError:
        return False

if len(argv) != 3 or isInt(argv[1]) == False or isInt(argv[2]) == False:
    print 'Usage: 02.py <num1> <num2>'
    exit(1)

print int(argv[1]) + int(argv[2])