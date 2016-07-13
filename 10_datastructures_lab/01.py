_author_ = 'mariag'

import sys

file_hosts = 'hosts.txt'
hostsDic = {}

#load key|value to dictionary
with open(file_hosts, 'r') as f_hosts:
    for line in f_hosts:
        host = line.split('=')[0] 
        ip = line.rstrip('\n').split('=')[1]
        hostsDic[host] = ip

for host_input in sys.argv[1:]:
    value = hostsDic.get(host_input,0)
    if value == 0:
        print "host:'%s' doesn't exist" % host_input
    else:
        print value
