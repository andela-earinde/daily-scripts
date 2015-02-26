#function for generating pig latin

def pig_latin(string, count=0):
	vow = ["a", "e", "i", "o", "u"]
	pig = string
	coun = count + 1
	if string[0] in vow and count == 0:
		return "%s%s" %(pig, "way")
	elif string[0] in vow and count != 0:
		return "%s%s" %(pig, "ay")	
	elif string[0] not in vow:
		pig = "%s%s" %(pig[1:], pig[0])
		return pig_latin(pig, coun)

	
