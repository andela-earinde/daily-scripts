#count the vowel in a string input

def count_vowel(string):
	vow = ["a", "e", "i", "o", "u"]
	count = 0
	for i in string:
		if i in vow:
			count += 1
	return count

#count the vowel in a string and return the sum
def count_vowel_sum(string):
	count = {"sum":0, "a":0, "e":0, "i":0, "o":0, "u":0}
	for i in string:
		if i in count:
			count["sum"] += 1
			count[i] += 1
	return "There are %d vowels, %d a, %d e, %d i,"\
	       "%d o and %d u"%(count["sum"], count["a"], count["e"],\
	        count["i"], count["o"], count["u"])

#Using list comprehension
def count_vowel(string):
	vow = ["a", "e", "i", "o", "u"]
	li = [i for i in string if i in vow]
	return len(li)


