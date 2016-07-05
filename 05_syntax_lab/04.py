_author_ = 'mariag'

sen = []
while True:
    print 'Please write a sentance'
    userInput = raw_input()
    if userInput == '':
        break
    sen.append(userInput)

for i in reversed(sen):
    print i