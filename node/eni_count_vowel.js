//count the vowel in a string input

function countVowel(string) {
	var vow = ["a", "e", "i", "o", "u"];
    var count = 0;
    for (var i = 0; i < string.length; i++) {
        if (vow.indexOf(string[i]) !== -1) {
        	count++;
        }	
    }
    return count;
}

function countVowelSum(string) {
	var count = {"sum":0,"a":0,"e":0,"i":0,"o":0,"u":0};
	for (var i = 0; i < string.length; i++) {
		if (string[i] in count) {
			count["sum"]++;
			count[string[i]]++;
		}
	}
	return "There are "+count["sum"]+" vowels, "+count["a"]+" a, "
	       +count["e"]+" e, "+count["i"]+" i, "+count["o"]+" o, "
	       +count["u"]+" u";
}