#!/usr/bin/node

const request = require('request');
const movieId = 3; // Example: 3 = "Return of the Jedi"
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }
  const json = JSON.parse(body);
  const characters = json.characters;
  characters.forEach(character => {
    console.log(character);
  });
});
