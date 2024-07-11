#!/usr/bin/node
// Prints all characters

if (process.argv.length !== 3) {
  process.exit();
}
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
const request = require('request');

// Recursive function
function printNextCharacter (urls) {
  // Remove first URL
  const characterURL = urls.shift();
  if (characterURL) {
    request(characterURL, function (error, response, body) {
      if (!error) {
        // Parse and print the character
        console.log(JSON.parse(body).name);
        // Move to next character
        printNextCharacter(urls);
      }
    });
  }
}

// Fetches a list
function printStarWarsCharacters (url) {
  // Get list of URL
  request(url, function (error, response, body) {
    if (!error) {
      // Call recursive function
      printNextCharacter(JSON.parse(body).characters);
    }
  });
}

printStarWarsCharacters(url);
