#functions for implementing complex numbers

#complex number addition
#note the arguments should be complex numbers written like: 1+5j
def comp_add(first, second):
	return complex(first) + complex(second)

def comp_sub(first, second):
	return complex(first) * complex(second)

def comp_div(first, second):
	return complex(first) / complex(second)

#invert the complex numbers
def comp_inv(comp):
	return -complex(comp)

#find the complex conjugate of a complex  number
def comp_conj(comp):
	com = complex(comp)
	return complex(com.real, -com.imag)
#find the modulus of a complex number
#the second argument is the number of digits to round the modulus
def comp_mod(comp, roun):
	com = complex(comp)
	return round(abs(com), roun)
