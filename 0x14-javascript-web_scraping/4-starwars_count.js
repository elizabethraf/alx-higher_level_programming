#!/usr/bin/node

const request = require("request");

const apiUrl = "https://swapi-api.alx-tools.com/api/films/";
const characterId = 18;

let count = 0;

request(apiUrl, (error, response, body) => {
    if (error) {
          console.log("Error:", error);
              return;
                }

      const data = JSON.parse(body);
        const films = data.results;

          films.forEach(film => {
                film.characters.forEach(character => {
                        if (character.includes(characterId)) {
                                  count++;
                                        }
                            });
                  });

            console.log(`Wedge Antilles is present in ${count} movies.`);
});

