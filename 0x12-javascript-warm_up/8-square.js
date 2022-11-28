#!/usr/bin/node
let count;
let wordc;
let myword = '';
if (process.argv.length > 2) {
  for (count = 0; count < parseInt(process.argv[2]); count++) {
    for (wordc = 0; wordc < parseInt(process.argv[2]); wordc++) {
      myword += 'X';
    }
    console.log(myword);
    myword = '';
  }
} else {
  console.log('Missing size');
}
