//coin flip simulation in javascript

function flipCoin(number) {
	var head = [];
	var tail = [];

	for(var i = 0; i < number; i++){
		var occur = Math.round(Math.random());
		if(occur === 1){
			head.push(1);
		}
		else {
			tail.push(0);
		}
	}

	return "You flipped the coin "+number+" times. The outcome is "
	       +head.length+" heads and "+tail.length+" tails";
}