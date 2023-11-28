#!/usr/bin/node

// Import the request node for sending HTTP/HTTPS requests
const request = require('request');

// use the comd line args to get url request
request.get(process.argv[2], function (error, response) {
	// check error
	if (error) {
		console.error(error);
	}
	console.log('code:', response && response.statusCode);
});
