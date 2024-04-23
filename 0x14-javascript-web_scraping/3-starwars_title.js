#!/usr/bin/node

const request = require('request');

// Check if movie ID is provided
if (process.argv.length < 3) {
  console.error('Please provide the movie ID as an argument.');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Making a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } else {
      console.error(`Failed to retrieve movie details. Status code: ${response.statusCode}`);
    }
  }
});
