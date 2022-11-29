#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let number = 0;

  for (counter; counter < list.length; counter++) {
    if (list[counter] === searchElement) {
      number++;
    }
  }
  return (number);
};
