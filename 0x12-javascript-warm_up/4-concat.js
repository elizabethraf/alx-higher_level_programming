#!/usr/bin/node
const process = require('process');
if (process.argv[2] === undefined) {
  console.log('undefined is undefined');
} else {
  console.log(process.argv[2]);
}
