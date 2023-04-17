#!/usr/bin/node

const process = require('process');

const fs = require('fs');
const { error } = require('console');
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (err, data) =>{
  if (err) throw error;
  console.log(data.toString());
})
