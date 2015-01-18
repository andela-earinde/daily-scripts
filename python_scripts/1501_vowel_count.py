#!/usr/bin/python

import sys

class StringOps:
    def count_vowels(self, word):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_count = 0
        for char in word:
            if char in vowels:
                vowel_count += 1

        return vowel_count

strops = StringOps()
word = sys.argv[1]
print strops.count_vowels(word)
