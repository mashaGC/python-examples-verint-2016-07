_author_ = 'mariag'

from random import randint

num = randint(1,100)

print 'Guess the number'

while True:
    flag = randint(1,20) #if flag is 7, write the incorrect response
    guess = int(raw_input())
    if guess == num:
        print 'Correct!!!'
        break
    if flag != 7:
        if guess > num:
            print 'Too high, guess again'
        elif guess < num:
            print 'Too low, guess again' 
    elif flag== 7:
        if guess > num:
            print 'Too low, guess again'
        elif guess < num:
            print 'Too high, guess again'