//function for generating pig latin

function pigLatin(string, count) {
	var vow = ["a", "e", "i", "o", "u"];
	pig = string;
	coun = count || 0;
	if (vow.indexOf(string[0]) !== -1 && coun === 0) {
		return pig+"way";
	}
	else if (vow.indexOf(string[0]) !== -1 && coun !== 0) {
		return pig+"ay";
	}
	else if (vow.indexOf(string[0]) === -1) {
		count++
		pig = pig.substring(1) + pig[0];
		return pigLatin(pig, coun);
	}
}