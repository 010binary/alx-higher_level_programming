#!/usr/bin/node

const request = require('request');

const getFilmCharacters = (filmId) => {
  return new Promise((resolve, reject) => {
    const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const filmData = JSON.parse(body);
        const characters = filmData.characters;
        resolve(characters);
      }
    });
  });
};

const getCharacterName = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
};

async function main () {
  try {
    const filmId = process.argv[2];
    const characters = await getFilmCharacters(filmId);

    for (const characterUrl of characters) {
      const characterName = await getCharacterName(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
}

main();
