#!/usr/bin/node
const process = require('process');

function factorial (number) {
  const n = parseInt(number);

  if (n === 0 || isNaN(n)) {
    return 1;
  }

  if (n > 0) {
    return (n * factorial(n - 1));
  }
}
const number = process.argv[2];
console.log(factorial(number));
