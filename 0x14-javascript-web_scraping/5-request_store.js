#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if URL and file path are provided
if (process.argv.length < 4) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected status code: ${response.statusCode}`);
    process.exit(1);
  }

  // Write the response body to the file
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
  });
});
