#!/usr/bin/node

// a script that prints all characters of a Star Wars movie:
// first argument is the Movie ID - example: 3 = “Return of the Jedi”
// one character name by line in the same order of the list “characters” in the /films/ response
// You must use the Star wars API
// You must use the module request

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach(character => {
    request.get(character, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
