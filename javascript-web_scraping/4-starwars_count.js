#!/usr/bin/node

const process = require('process');
const url = process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const moviesList = JSON.parse(body).results;

    let counter = 0;
    for (const movies of moviesList) {
      for (const character of movies.characters) {
        if (character.includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
