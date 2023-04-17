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
    jsonBody.forEach(user => {
      if (user.completed) {
        if (counter[user.userId] === undefined) {
          counter[user.userId] = 1;
        } else {
          counter[user.userId]++;
        }
      }
    });
    console.log(counter);
  }
});
