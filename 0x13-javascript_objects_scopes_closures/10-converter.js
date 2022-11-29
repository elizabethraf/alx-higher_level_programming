#!/usr/bin/node
exports.converter = function (base) {
  if (base === 10) {
    return function (convNumber) {
      return (convNumber).toString(base);
    };
  } else {
    return function (convNumber) {
      return parseInt(convNumber, base);
    };
  }
};
