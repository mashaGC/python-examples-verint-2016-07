_author_ = 'mariag'

import re
lines = [line.rstrip('\n') for line in open('input.csv')]

for line in lines:
    m = re.search('^([^,]*),([^,]*),(.*)', line)
    print "{},{},{}".format(m.group(2),m.group(1),m.group(3))