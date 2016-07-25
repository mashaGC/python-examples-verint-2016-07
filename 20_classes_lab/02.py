_author_ = 'mariag'

class MyCounter(object):
    count = 0
    def __init__(self):
        MyCounter.count += 1

for _ in range(10):
     c1 = MyCounter()

# should print 10
print MyCounter.count