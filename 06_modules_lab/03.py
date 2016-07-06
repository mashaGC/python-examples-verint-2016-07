_author_ = 'mariag'

from sys import argv
import os

if len(argv)!= 3:
    print 'usage: <03.py> <dir path> <size[MB]>'
    exit(1)

dirPath = argv[1]
sizeLimit = int(argv[2])

for root, dirs, files in os.walk(dirPath):
    for name in files:
        size = os.stat(name).st_size >> 20
        if  size > sizeLimit:
            print 'The file {} size is {}MB'.format(name, size)
            answer = raw_input('Would you like to delete it? (Y/N): ')
            if (answer.upper() == 'Y'):
                os.remove(name)
                print 'File {} was deleted'.format(name)
            elif (answer.upper() == 'N'):
                print 'File {} wasn\'t deleted'.format(name)

print 'No more large files'

