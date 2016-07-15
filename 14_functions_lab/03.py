_author_ = 'mariag'

def sum_dec(*args):
    res = 0
    for num in args:
        if type(num) != int:
            raise Exception ("sum_dec expects integer")
        num_str = str(num)
        if len(num_str)>1:
            res += int(num_str[-2])
    return res

print sum_dec(1233,4,23,145) #expect 9