#!/usr/bin/node

// Import the fs module, which helps interract with file with things
// such as write, read etc
const fs = require('fs');

// retrieve the file path and data from the cmd line args
const filePath = process.argv[2];
const content = process.argv[3];

// write the content of the file
// the write function will have 4 args: path, content, encoding, callback function
fs.writeFile(filePath, content, 'utf-8', (err) => {
  // check for error
  if (err) {
    console.error(err);
  }
  // else {
  // console.log('File has been written successfully!');
  // }
});
