#reverse string projects

def reverse(string):
	s = ""
	m = -1
	for i in string:
		s = s + string[m]
		m = m - 1
	print s