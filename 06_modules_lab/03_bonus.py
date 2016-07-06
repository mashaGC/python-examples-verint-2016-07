_author_ = 'mariag'

from sys import argv
import argparse
import os

parser = argparse.ArgumentParser(description='Dir path and max size file')
parser.add_argument("dirPath", type=str, help='path to the directory')
parser.add_argument("sizeLimit", type=int, help='minimum size of file')

args = parser.parse_args()

for root, dirs, files in os.walk(args.dirPath):
    for name in files:
        size = os.stat(name).st_size >> 20
        if  size > args.sizeLimit:
            print 'The file {} size is {}MB'.format(name, size)
            answer = raw_input('Would you like to delete it? (Y/N): ')
            if (answer.upper() == 'Y'):
                os.remove(name)
                print 'File {} was deleted'.format(name)
            elif (answer.upper() == 'N'):
                print 'File {} wasn\'t deleted'.format(name)

print 'No more large files'

