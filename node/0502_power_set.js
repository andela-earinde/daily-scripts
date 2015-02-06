function powerSet (array) {
  var result = [];

  for (var i = 0; i < (Math.pow(2, array.length)); i++) {
    var binaryRep = i.toString(2);
    binaryRep = padBinary(binaryRep, array.length);
    var set = [];

    for (var key in binaryRep) {
      if (binaryRep[key] === "1") {
        set.push(array[key]);
      }
    }

    result.push(set);
  }

  return result;
}

function padBinary (binary, stringLength) {
  var len = binary.length;
  var rem = stringLength - binary.length;

  var padding = "";
  for (var i = 0; i < rem; i++) {
    padding += "0";
  }

  return padding + binary;
}
