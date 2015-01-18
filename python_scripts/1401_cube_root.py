#!/usr/bin/python

import sys

class Calculator:
    def cube_root(self, number, guess=1.0):
        if '{:.2f}'.format(guess ** 3) == '{:.2f}'.format(number):
            return guess

        return self.cube_root(number, ((number / (guess ** 2)) + 2 * guess) / 3.0)

calc = Calculator()
test_number = int(sys.argv[1])
print calc.cube_root(test_number)
