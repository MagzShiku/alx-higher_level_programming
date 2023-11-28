#!/usr/bin/node

// Import the request node for sending HTTP/HTTPS requests
const request = require('request');

// use the comd line args to get url request
request.get(process.argv[2])
	.on('response', function (response) {
		// print the status code on console
		console.log('code:, ${statusCode)}');
	});
