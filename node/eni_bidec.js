//Binary to Decimal and vice versa implemented in javascript

function converter(number, base) {
	if(base === 2){
		return Number(number.toString(2));
	}
	else if(base === 10){
		return parseInt(number, 10);
	}
}