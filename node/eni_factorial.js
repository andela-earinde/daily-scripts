//Factorial finder in javascript

//using recursion
function recFact(number) {
	if(number === 0){
		return 1;
	}
	else if(number === 1){
		return 1;
	}
	else{
		return number * recFact(number - 1);
	}
}

//Using loops
function loopFact(number) {
	var num = 1;
	for(var i = 1; i <= number; i++){
		num *= i;
	}
	return num;
}