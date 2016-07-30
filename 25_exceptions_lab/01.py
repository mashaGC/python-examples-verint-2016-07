_author_ = 'mariag'

import math

while True:
    num = 0
    input = raw_input()
    if input == "":
        break
    try:
        num = float(input) 
    except ValueError as e:
        print "{} is not a number. Try again".format(input)
        continue
    try:
        res = math.sqrt(num)
        print "Sqrt({})={}".format(input,round(res,3))
    except ValueError as e:
        print "{} is negative. Try again".format(input)