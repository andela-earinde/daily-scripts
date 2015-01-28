function deepObjects (object, property) {
  if (typeof object[property] !== 'object') {
    return object[property];
  } else {
    return deepObjects(object[property], property);
  }
}

var object = JSON.parse(process.argv[2]);
var property = process.argv[3][0];
console.log(deepObjects(object, property));
