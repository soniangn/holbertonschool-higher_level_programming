#!/usr/bin/node
const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let x = process.argv[2]; x > 0; x--) {
    console.log('X'.repeat(process.argv[2]));
  }
}
