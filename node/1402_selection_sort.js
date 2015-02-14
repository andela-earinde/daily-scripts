function selectionSort (list) {
  var sortedList = list.slice(0);
  for (var idx in list) {
    var minimumValue = list[idx];
    var minimumIndex = +idx;
    var nextIndex = +idx + 1;

    while (nextIndex < list.length) {
      if (list[nextIndex] < minimumValue) {
        minimumValue = list[nextIndex];
        minimumIndex = nextIndex;
      }
      nextIndex += 1;
    }


    // Swap minimumValue with the element at the current index
    var temp = list[idx];
    list[idx] = list[minimumIndex];
    sortedList[idx] = list[minimumIndex];
    list[minimumIndex] = temp;
    sortedList[minimumIndex] = temp;
  }

  return sortedList;
}

console.log(selectionSort([4, 3, 2, 1]));
