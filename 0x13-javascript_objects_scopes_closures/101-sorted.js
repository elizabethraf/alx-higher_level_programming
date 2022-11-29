#!/usr/bin/node
const dict = require('./101-data.js').dict;
console.log(dict);
const newdict = {};
Object.keys(dict).map(function (num, index) {
  return num * index;
});
console.log(newdict);
