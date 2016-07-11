_author_ = 'mariag'

from sys import argv

if len(argv)!= 3:
    print 'usage: <01.py> <file_name1> <file_name2>'
    exit(1)

file_name1 = argv[1]
file_name2 = argv[2]

with open(file_name1, 'r') as f_from:
    with open(file_name2, 'a') as f_to:
        f_to.write('\n')
        for line in f_from:
            f_to.write(line)