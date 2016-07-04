_author_ = 'mariag'

for i in range(10):
    print 'Please insert a number. Count ', i+1
    newInput = float(raw_input())
    if i==0:
        largest = newInput
    if largest < newInput:
        largest = newInput
print 'largest is: ', largest