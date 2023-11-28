#!/usr/bin/node

// script that gets the contents of a webpage and stores it in a file.
// import Request to manipulate file systems
const request = require('request');

// Get URL and file path from command line args
const url = process.argv[2];
const filePath = process.argv[3];

// pull request
request(url, (error, response, body) => {
  // check for error
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Write body to file
  require('fs').writeFile(filePath, body, 'utf-8', err => {
    if (err) {
      console.error('Error writing file:', err);
    } else {
      console.log('File written successfully');
    }
  });
});
