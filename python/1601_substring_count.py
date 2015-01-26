#!/usr/bin/python

import sys

class StringOps:
    def count_substring(self, word, sub):
        sub_count = 0
        for i in range(len(word)):
            if word[i] == sub[0]:
                if word[i:len(sub) + i] == sub:
                    sub_count += 1

        return sub_count

strops = StringOps()
word = sys.argv[1]
sub = sys.argv[2]
print strops.count_substring(word, sub)
