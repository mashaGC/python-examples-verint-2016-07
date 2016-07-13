_author_ = 'mariag'

import sys

file_hosts = 'hosts.txt'
hostsDic = {}

#load key|value to dictionary
with open(file_hosts, 'r') as f_hosts:
    for line in f_hosts:
        host, ip = line.rstrip('\n').split('=')
        hostsDic[host] = ip

for host_input in sys.argv[1:]:
    if host_input in hostsDic:
        print hostsDic.get(host_input)
    else:
        print "host:'{}' doesn't exist".format(host_input)
