_author_ = 'mariag'

from random import randint

num1 = randint(1,10)
num2 = randint(1,10)

print "num1: {}; num2: {}".format(num1, num2)

for i in range(num1,num1*num2+1):
    if (i%num1 == 0) and (i%num2 == 0):
        print i
        break