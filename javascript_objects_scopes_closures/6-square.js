#!/usr/bin/node

const Parent = require('./5-square');

class Square extends Parent {
  charPrint (c = 'X') {
    for (let x = 0; x < this.width; x++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
