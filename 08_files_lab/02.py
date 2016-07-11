_author_ = 'mariag'

import sys
from itertools import izip_longest

if len(sys.argv)!= 4:
    print 'usage: <02.py> <file_name1> <file_name2> <file_name_new>'
    exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]
file_new = sys.argv[3]

with open(file_new, 'w') as f_to:
    with open(file1, 'r') as f_from1:
        with open(file2, 'r') as f_from2:
            a = iter(izip_longest(f_from1, f_from2, fillvalue=''))
            for i in a:
                f_to.write(i[0])
                f_to.write(i[1])