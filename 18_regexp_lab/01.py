_author_ = 'mariag'

import re
import sys



file_key_value = sys.argv[1]
input_key = sys.argv[2]
kvDic = {}


#load key|value to dictionary
with open(file_key_value, 'r') as f_kv:
    for line in f_kv:
        m = re.search('^(\w+)\s*=\s*(\w+)' , line)
        if m is not None:
            key = m.group(1)
            value = m.group(2)
            kvDic[key] = value

if kvDic.has_key(input_key):
    print input_key," = ",
    print kvDic.get(input_key)
else:
    print "key:'{}' doesn't exist".format(input_key)
