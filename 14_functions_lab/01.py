_author_ = 'mariag'

def mysum(*args):
    ints = [i for i in args if type(i) == int] 
    return sum(ints)

#primes = [x for x in range(2, 50) if x not in noprimes]

def mymul(*args):
    ints = [i for i in args if type(i) == int]
    return reduce(lambda x, y: x*y, ints)


print mysum('1',2,3)
print mymul('1',2,3,'4',5)