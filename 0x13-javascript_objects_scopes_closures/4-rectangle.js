#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      console.log('X'.repeat(this.width));
    }
  }
}

rotate() {
  ctx.rotate(angle);
  this.width = this.width;
  this.height += this.height;
  this.width -= this.height;
}

 double();
  this.width = this.width * 2;
  this.height = this.height * 2;

module.exports = Rectangle;
