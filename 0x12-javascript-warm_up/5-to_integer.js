#!/usr/bin/node
const process = require('process');
if (isNaN(parseInt(process.argv[2])) === false) {
  console.log('Not a number');
} else if (process.argv.length === 3) {
  console.log(process.argv[2] + 'My number: 89');
} else if (process.argv.length === 4) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
