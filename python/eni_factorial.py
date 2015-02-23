#Factorial finder

if __name__ == "__name__":
	print "This a module prints out the factorial of a number"\
	      "it uses loop and recursion"

def rec_fact(number):
	if number == 0:
		return 1;
	elif number == 1:
		return 1;
	else:
		return number * rec_fact(number - 1)

def loop_fact(number):
	num = 1;
	for i in range(1, number+1):
		num *= i;
	return num




