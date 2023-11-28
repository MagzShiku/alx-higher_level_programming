#!/usr/bin/node

const fs = require('fs');
// imports the fs module which allows us to interract with file system
// could be through write, appent, join etc
const filePath = process.argv[2];
// we create a variable
// this retrieves the file path from cml args in this casr 1
fs.readFile(filePath, 'utf-8', function (err, data) {
	// reads the file
	if (err) {
		// if there is an error reading the data show the error
		console.error(err);
		return;
	} else {
		// if read, the pront the content of the file onto console
		console.log(data);
	}
});
