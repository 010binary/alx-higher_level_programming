#!/usr/bin/node

const request = require('request');

// Check if API URL is provided
if (process.argv.length < 3) {
  console.error('Usage: ./4-starwars_count.js <api_end_point>');
  process.exit(1);
}

let num = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          num += 1;
        }
      });
    });
    console.log(num);
  }
});
