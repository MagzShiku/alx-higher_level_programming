#!/usr/bin/node

// Import the request module, which allows us to send HTTP/HTTPS requests
const request = require('request');

// Retrieve the API URL from the command line arguments
const apiUrl = process.argv[2];

// Send a GET request to the API URL using the request module
request.get(apiUrl, (error, response, body) => {
  // Check if an error occurred during the request
  if (error) {
    // If an error occurred, log the error message to the console
    console.error(error);
    return;
  }

  // Parse the response body to JSON format
  const todosData = JSON.parse(body);

  // Create an object to store the number of completed tasks by user ID
  const completedTasksByUser = {};

  // Loop through the todos data and count the completed tasks for each user
  todosData.forEach((todo) => {
    // Check if the task is completed
    if (todo.completed) {
      // Increment the completed tasks count for the user
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  // Print the completed tasks count by user ID to the console
  console.log(completedTasksByUser);
});
