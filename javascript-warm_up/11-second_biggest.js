#!/usr/bin/node
const process = require('process');

if (process.argv.length > 3) {
  const arg = process.argv.slice(2).sort((function(a, b){return a - b}));
  const length = arg.length;
  console.log(arg[length - 2]);
} else {
  console.log('0');
}
