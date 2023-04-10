#!/usr/bin/node
const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let x = process.argv[2]; x > 0; x--) {
    console.log('C is fun');
  }
}
