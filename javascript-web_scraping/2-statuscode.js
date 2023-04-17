#!/usr/bin/node

const process = require('process');
const url = process.argv[2];
const request = require('request');

request(url, function (error, response) {
  if (error) console.log(error);
  console.log('code: ', response.statusCode);
});
