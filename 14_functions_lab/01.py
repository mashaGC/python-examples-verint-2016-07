_author_ = 'mariag'

def mysum(*args):
    sum = 0
    for i in args:
        if type(i) == int:
            sum += i
    return sum


def mymul(*args):
    mul = 1
    for i in args:
        if type(i) == int:
            mul *= i
    return mul


print mysum('1',2,3)
print mymul('1',2,3,'4',5)