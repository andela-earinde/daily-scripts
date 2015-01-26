#!/usr/bin/python

import sys

class Towers:
    def print_move(self, fro, to):
        print 'Move from ' + str(fro) + ' to ' + str(to)

    def move(self, n, fro, to, spare):
        if n == 1:
            self.print_move(fro, to)
        else:
            self.move(n - 1, fro, spare, to)
            self.move(1, fro, to, spare)
            self.move(n - 1, spare, to, fro)

no_of_pegs = int(sys.argv[1])
towers = Towers()
towers.move(no_of_pegs, 'A', 'B', 'C')
