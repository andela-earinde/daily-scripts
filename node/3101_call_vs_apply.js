'use strict';

function callVsApply (func, arg) {
   var argumentList = Array.prototype.slice.call(arguments);

   return Object.prototype.toString.call(argumentList[1]) === '[object Array]' ? func.apply(this, argumentList[1]) : func.call(this, argumentList[1]);
}

function callVsApplyTests () {
  var reverseString = function (word) {
    return word.split("").reverse().join("");
  };

  console.assert(callVsApply(reverseString, "hello") === "olleH", "'Hello' reversed should be 'olleH'");
}

callVsApplyTests();
