#!/usr/bin/node

const process = require('process');
const url = process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const jsonBody = JSON.parse(body);
    const counter = {};
    for (const user of jsonBody) {
      if (user.completed) {
        if (counter[user.userId] === undefined) {
          counter[user.userId] = 0;
        } else {
          counter[user.userId]++;
        }
      }
    }
    console.log(counter);
  }
});
