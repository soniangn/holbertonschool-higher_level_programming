#!/usr/bin/node
const process = require('process');

function factorial(number) {
    let n = parseInt(number);

    if (n === 0 || isNaN(n)) {
      return 1;
    }
    
    if (n > 0) {
      return (n * factorial(n - 1));
    }
}

console.log(factorial(process.argv[2]));
