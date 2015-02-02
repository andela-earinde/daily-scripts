'use strict';

var SumOfMultiples = function (array) {
  var result = {};

  result.factors = array || [3, 5];

  result.to = function (limit) {
    var multiples = [];

    for (var i = 1; i < limit; i++) {
      for (var key in this.factors) {
        if (i % this.factors[key] === 0 && multiples.indexOf(i) <= -1) {
          multiples.push(i);
        }
      }
    }

    var sum = 0;
    for (var newKey in multiples) {
      sum += multiples[newKey];
    }

    return sum;
  };

  return result;
};

var array = JSON.parse(process.argv[2]);
var limit = +process.argv[3];

console.log(SumOfMultiples(array).to(limit))
