#!/usr/bin/python
import sys

class Calculator:
    def square(self, num):
        return reduce(lambda x,y: x + y, [num for x in xrange(num)])

calc = Calculator()
number = int(sys.argv[1])
print calc.square(number)
