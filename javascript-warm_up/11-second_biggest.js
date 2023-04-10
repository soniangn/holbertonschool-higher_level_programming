#!/usr/bin/node
const process = require('process');

if (process.argv.length > 3) {
  const arg = process.argv.slice(2).sort();
  const length = arg.length;
  console.log(arg[length - 2]);
} else {
  console.log('0');
}
