_author_ = 'mariag'

sen = []
while True:
    print 'Please write a sentance'
    userInput = raw_input()
    if userInput == '':
        break
    sen.append(userInput)

amount = len(sen)
for i in range(amount):
    print sen[amount-i-1]