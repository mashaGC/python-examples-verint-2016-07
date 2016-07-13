_author_ = 'mariag'

from sys import argv

if len(argv)!= 3:
    print 'usage: <01.py> <file_from> <file_to>'
    exit(1)

file_from = argv[1]
file_to = argv[2]

with open(file_from, 'r') as f_from:
    with open(file_to, 'a') as f_to:
        f_to.write('\n')
        for line in f_from:
            f_to.write(line)