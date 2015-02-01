#!/usr/bin/python

import sys

class Fibonacci:
    '''
    This class creates an instance that can be used to compute the value of the fibonacci sequence at a specified position in the sequence.
    '''
    cache = []
    def compute(self, n):
        if self.cache[n] != 0:
            return self.cache[n]
        else:
            if n <= 1:
                self.cache[n] = 1
                return self.cache[n]
            else:
                self.cache[n] = self.compute(n - 1) + self.compute(n - 2)
                return self.cache[n]

    def compute_memoized(self, n):
        self.cache = map(lambda x: 0, range(n + 1))
        return self.compute(n)

position = int(sys.argv[1])
calculator = Fibonacci()
print calculator.compute_memoized(position)
