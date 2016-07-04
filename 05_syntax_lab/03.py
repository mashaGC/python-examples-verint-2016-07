_author_ = 'mariag'

from random import randint

numInt = randint(1,10000)
numStr = str(numInt)

sum = 0
for dig in numStr:
    sum += int(dig)

print "Num is {}, sum of digits is {}".format(numInt, sum)