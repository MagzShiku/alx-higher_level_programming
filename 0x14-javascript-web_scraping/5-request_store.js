#!/usr/bin/node

// script that gets the contents of a webpage and stores it in a file.
// import Request to manipulate file systems
const request = require('request');
const fs = require('fs');

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
	fs.writeFile(filePath, body, 'utf8', (error) => {
		if (error) {
			console.error(error);
		} else {
			console.log(`Content successfully written to ${filePath}`);
		}
	});
});
