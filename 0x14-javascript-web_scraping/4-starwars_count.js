#!/usr/bin/node

// prints the number of movies where the character “Wedge Antilles” is present
// import request module
const request = require('request');

// Retrieve the API URL from the command line arguments
const apiUrl = process.argv[2];

// Define the character ID for "Wedge Antilles"
const characterId = 18;

// Get request to the API url
request.get(apiUrl, (error, response, body) => {
  // check for error
  if (error) {
    console.error(error);
    return;
  }

  // parse the response body into JSON format
  const filmsData = JSON.parse(body);

  // Filter the films where "Wedge Antilles" is present
  const filmsWithWedge = filmsData.results.filter((film) => {
    const characters = film.characters;
    return characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
  });

  // count the number of films that have "Wedge Antilles"
  const count = filmsWithWedge.length;

  // print the counts of these instances to console
  console.log(count);
});
