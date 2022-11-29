#!/usr/bin/node
const dict = require('./101-data.js').dict;
console.log(dict);
const newdict = {};
Object.keys(dict).map(function (num, index) {
  if (newdict[dict[key]] === undefined) {
    newdict[dict[key]] = [];
  }
  newdict[dict[key]].push(key);
});
console.log(newdict);
