#!/usr/bin/node
// Write a class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // this prints a rectangle with X
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    // exchanges the width and the height of the rectangle stores the value in tmp so that it can exchange
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    // this multiples the width and the height of the rectangle by 2
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
