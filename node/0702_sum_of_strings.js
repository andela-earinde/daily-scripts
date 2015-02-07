function sumStrings(a,b) { 
  var result = '';
  var longerString = a.length > b.length ? a : b;
  var shorterString = longerString === a ? b : a;
  longerString = longerString.split('').reverse().join('');
  shorterString = shorterString.split('').reverse().join('');
  var carry = 0;  
  for (var key in longerString) {
    var remainder = ((+longerString[key] || 0) + (+shorterString[key] || 0) + carry) % 10;
    carry = Math.floor(((+longerString[key] || 0) + (+shorterString[key] || 0) + carry) / 10);
    result += remainder;
  }
  result = carry ? result + carry : result;
  var resultArray = result.split('').reverse();
  resultArray = resultArray[0] === '0' ? resultArray.slice(1) : resultArray;
  return resultArray.join('');
}

var firstString = process.argv[2];
var secondString = process.argv[3];
console.log(sumStrings(firstString, secondString));
