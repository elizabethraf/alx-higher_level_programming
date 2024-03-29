#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(`Characters in ${film.title} :`);
    film.characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.log(`Error requesting character: ${error}`);
        }
      });
    });
  } else {
    console.log(`Error requesting film: ${error}`);
  }
});
