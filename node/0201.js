function truthTable (varCount) {
     
    for (var i = 0; i < Math.pow(2, varCount); i++) {

        // Store the binary representation of the current value of the counter
        var binaryRep = i.toString(2);

        // Create the padding. This is a string consisting of zeroes.
        var padding = new Array(varCount - binaryRep.length + 1).join('0');

        // Convert the binary representation to a string of "T"s and "F"s.
        var converted = (padding + binaryRep)
                            .split('')
                            .map(function (elem) {
                                return ((!!(+elem) + '')[0]).toUpperCase();
                            })
                            .join(' ');

        console.log(converted);
    }

}

var count = +(process.argv[2]);
console.log('Now timing the creation of a truth table with ' + count + ' variables');
var start = Date.now();
truthTable(count);
console.log((Date.now() - start) + ' ms\t', Math.pow(2, count) + ' rows');
