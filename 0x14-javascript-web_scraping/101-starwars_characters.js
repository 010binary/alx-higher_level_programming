#!/usr/bin/node

const request = require('request');

const getFilmData = (filmId) => {
  return new Promise((resolve, reject) => {
    const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const getCharacterData = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

async function main () {
  try {
    const filmId = process.argv[2];
    const filmData = await getFilmData(filmId);

    const characters = filmData.characters;
    for (const character of characters) {
      const characterData = await getCharacterData(character);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

main();
