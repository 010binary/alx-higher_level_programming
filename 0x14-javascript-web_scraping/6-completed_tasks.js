#!/usr/bin/node

const request = require('request');

// Check if API URL is provided
if (process.argv.length < 3) {
  console.error('Please provide the API URL as an argument.');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make a request to the provided API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected status code: ${response.statusCode}`);
    process.exit(1);
  }

  // Parse the response body as JSON
  const todos = JSON.parse(body);

  // Initialize an object to store the number of completed tasks for each user ID
  const completedTasksByUser = {};

  // Iterate through the todos and count completed tasks for each user ID
  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  // Print the number of completed tasks for each user ID
  console.log(completedTasksByUser);
});
