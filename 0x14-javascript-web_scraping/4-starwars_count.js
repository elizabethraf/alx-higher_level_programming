#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.endsWith(`/${characterId}/`)) {
          count++;
        }
      });
    });
    console.log(`Wedge Antilles is present in ${count} films.`);
  } else {
    console.log('Error:', error);
  }
});
