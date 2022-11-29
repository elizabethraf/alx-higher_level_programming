#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let counter = 0; counter < list.length; counter++); {
    if (list[counter] === searchElement) {
      counter++;
    }
  }
  return (counter);
};
