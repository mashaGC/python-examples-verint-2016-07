_author_ = 'mariag'

from random import randint

num1 = randint(1,20)
num2 = randint(1,20)

print "num1: {}; num2: {}".format(num1, num2)

fact1 = [1]
fact2 = [1]

#find the factorials of num1 and num2
i = 2
while num1 != 1:
    if (num1 % i == 0):
        fact1.append(i)
        num1 = num1/i
    else:
        i += 1

i = 2
while num2 != 1:
    if (num2 % i == 0):
        fact2.append(i)
        num2 = num2/i
    else:
        i += 1

print fact1
print fact2

#find the least common multiplier
i = 0
j = 0
result = 1
while (i < len(fact1) or j < len(fact2)):
    if (i == len(fact1) and j < len(fact2)):
        result*=fact2[j]
        j+=1
    elif (i < len(fact1) and j == len(fact2)):
        result*=fact1[i]
        i+=1
    elif(fact1[i] == fact2[j]):
        result *= fact1[i]
        i += 1
        j += 1
    elif(fact1[i] > fact2[j]):
        result *= fact2[j]
        j += 1
    elif(fact1[i] < fact2[j]):
        result *= fact1[i]
        i += 1
    
print result