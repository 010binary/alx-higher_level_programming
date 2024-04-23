#!/usr/bin/node

const request = require('request');

// Check if API URL is provided
if (process.argv.length < 3) {
  console.error('Usage: ./4-starwars_count.js <api_end_point>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = '18'; // Wedge Antilles' character ID

// Make a request to the Star Wars API
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
  const data = JSON.parse(body);

  const filmsWithWedgeAntilles = data.results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(filmsWithWedgeAntilles.length);
});
