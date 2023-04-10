#!/usr/bin/node
const process = require('process');

function add (a, b) {
  return parseFloat(a) + parseFloat(b);
}

console.log(add(process.argv[2], process.argv[3]));
