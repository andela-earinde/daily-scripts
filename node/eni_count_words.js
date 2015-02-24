//count the number of words in a string

function countString(string) {
	var arr = string.split(/\s/)
	return arr.length;
}