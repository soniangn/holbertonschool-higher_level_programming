#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const filename = process.argv[2];
const data = process.argv[3];

fs.writeFileSync(filename, data, (err, data) => {
  if (err) {
    console.log(err);
  }
});
