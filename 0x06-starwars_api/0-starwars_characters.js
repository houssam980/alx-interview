#!/usr/bin/node


if (process.argv.length !== 3) {
    process.exit();
  }
  const movieID = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
  const request = require('request');
  

  function printCharacter(urs) {
    const characterURL = urs.shift();
    if (characterURL) {
      request(characterURL, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
          printCharacter(urs);
        }
      });
    }
  }
  

  function printWarsCharacters (url) {
    request(url, function (error, response, body) {
      if (!error) {
        printCharacter(JSON.parse(body).characters);
      }
    });
  }
  
  printWarsCharacters(url);
