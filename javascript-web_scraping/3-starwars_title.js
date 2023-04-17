#!/usr/bin/node

const process = require('process');
const id = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
