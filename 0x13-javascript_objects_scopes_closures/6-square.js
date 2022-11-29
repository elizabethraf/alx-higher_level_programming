#!/usr/bin/node
const Rectangle = require('./5-square.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      for (let a = 0; a < this.height; a++) {
        console.log('X'.repeat(this.width));
      }
    }
    if (c) {
      for (let b = 0; b < this.height; b++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
