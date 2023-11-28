#!/usr/bin/node

// Import the request module, which allows us to send HTTP/HTTPS requests
const request = require('request');

// Retrieve the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API endpoint using the movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to the specified URL using the request module
request.get(url, (error, response, body) => {
  // Check if an error occurred during the request
  if (error) {
    // If an error occurred, log the error message to the console
    console.error(error);
    return;
  }

  // Parse the response body to JSON format
  const movieData = JSON.parse(body);

  // Retrieve the characters of the movie from the response data
  const characters = movieData.characters;

  // Print each character name to the console
  characters.forEach((characterUrl) => {
    // Send a GET request to the character URL
    request.get(characterUrl, (error, response, body) => {
      // Check if an error occurred during the request
      if (error) {
        // If an error occurred, log the error message to the console
        console.error(error);
        return;
      }

      // Parse the response body to JSON format
      const characterData = JSON.parse(body);

      // Retrieve the character name from the response data
      const characterName = characterData.name;

      // Print the character name to the console
      console.log(characterName);
    });
  });
});
