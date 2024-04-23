#!/usr/bin/node
const request = require('request');

// Check if URL is provided
if (process.argv.length < 3) {
  console.error('Please provide the URL to request as an argument.');
  process.exit(1);
}

const url = process.argv[2];

// Making a GET request to the provided URL
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
