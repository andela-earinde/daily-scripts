var Set = function (initialElementsArray) {
  this.initialElements = initialElementsArray;
  this.elements = this.createSet();
};

Set.prototype.add = function (element) {
  if (this.elements.indexOf(element) < 0) {
    this.elements.push(element);
  }

  return this.elements;
};

Set.prototype.createSet = function () {
  var distinctElements = [];
  this.initialElements.forEach(function (element) {
    if (distinctElements.indexOf(element) < 0) {
      distinctElements.push(element);
    }
  });
  return distinctElements;
};

Set.prototype.valueOf = function () {
  return this.elements;
};

Set.prototype.union = function (otherSet) {

};

Set.prototype.intersect = function (otherSet) {

};
