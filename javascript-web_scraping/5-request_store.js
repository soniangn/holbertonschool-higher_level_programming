#!/usr/bin/node

const process = require('process');
const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFileSync(filePath, body);
});
