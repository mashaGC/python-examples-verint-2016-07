_author_ = 'mariag'

class Summer(object):
    _sum = 0
    def __init__(self, _sum = 0):
        self._sum = _sum

    def add(self, *nums):
        for num in nums:
            self._sum += num

    def total(self):
        return self._sum

s = Summer()
t = Summer()
my_try = Summer(15)

s.add(10, 20)
t.add(50)
s.add(30)
my_try.add(1,1,1)

# should print 60
print s.total()

# should print 50
print t.total()

#should print 18
print my_try.total()