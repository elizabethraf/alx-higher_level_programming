#!/usr/bin/node

const request = require('request');
const episodeNumber = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
