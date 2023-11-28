#!/usr/bin/node

// Import necessary modules
const request = require('request');
const fs = require('fs');

// Get URL and file path from command line args
const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the specified URL
request(url, (error, response, body) => {
  // Check for errors during the request
  if (error) {
    console.error(error);
    return;
  }

  // Write the content of the response to the specified file path
  try {
    fs.writeFile(filePath, body, 'utf8', (err, result) => {
      if (err) {
        console.log(err);
      } else {
        console.log(`Content successfully written to ${filePath}`);
      }
    });
  } catch (err) {
    console.log(err);
  }
});
