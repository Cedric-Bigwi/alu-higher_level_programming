#!/usr/bin/node
const Square = require('./5-square');
class SquareExtended extends Square {
  charPrint(c) {
    let char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = SquareExtended;
