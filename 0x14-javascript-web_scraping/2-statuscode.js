#!/usr/bin/node

// Import the request node for sending HTTP/HTTPS requests
const request = require('request');

// Retrieve url to request fom CMD line args
const url = process.argv[2];

// send a GET request
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }

  // retrieve status code from response object
  const statusCode = response.statusCode;

  // print the status to the consile
  console.log('code:', statusCode);
});
