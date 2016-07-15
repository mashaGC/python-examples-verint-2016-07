_author_ = 'mariag'

import collections

def groupby(func, *args):
    res_dict = collections.defaultdict(list)
    for arg in args:
        res = func(arg)
        res_dict[res].append(arg)
    return res_dict

print groupby(lambda(s):s%2==0, 123, 25, 16, 256, 456)