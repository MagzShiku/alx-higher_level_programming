#!/usr/bin/node

// import request
const request = require('request');

// retrieve movie ID
const movieId = process.argv[2];

// construct URL for the movie
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to the specified URL using the request module
request.get(url, (error, response, body) => {
  // check for error
  if (error) {
    console.error(error);
    return;
  }

  // parse response into JSON format
  const movieData = JSON.parse(body);

  // Retrieve the title of the movie from the response data
  const movieTitle = movieData.title;

  // print title of movie onto console
  console.log(movieTitle);
});
