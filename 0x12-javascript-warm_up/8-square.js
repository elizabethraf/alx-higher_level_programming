#!/usr/bin/node
let count;
if (process.argv.length > 2) {
  for (count = 0; count < parseInt(process.argv[2]); count++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
} else {
  console.log('Missing size');
}
