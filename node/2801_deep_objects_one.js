function deepObjects (object, property) {
  for (var key in Object.keys(object)) {
    var value = Object.keys(object)[key];
    if (object.hasOwnProperty(value)) {
      if (typeof object[value] === 'object') {
        return deepObjects(object[value], property);
      } else if (value === property) {
        return object[value];
      } else {
        return "Property not found.";
      }
    }
  }
}

var object = JSON.parse(process.argv[2]);
var property = process.argv[3];
console.log(deepObjects(object, property));
