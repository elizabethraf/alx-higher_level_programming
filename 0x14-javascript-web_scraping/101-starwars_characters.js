#!/usr/bin/node

const request = require('request');
const async = require('async');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(`Characters in ${film.title} :`);
    async.mapSeries(film.characters, (characterUrl, callback) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          callback(null, character.name);
        } else {
          callback(`Error requesting character: ${error}`);
        }
      });
    }, (err, results) => {
      if (err) {
        console.log(err);
      } else {
        results.forEach(name => console.log(name));
      }
    });
  } else {
    console.log(`Error requesting film: ${error}`);
  }
});
