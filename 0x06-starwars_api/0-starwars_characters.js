#!/usr/bin/node
/**
  prints all characters of a Star Wars movie
  */

  const request = require('request');

  const movieId = process.argv[2];
  
  if (!movieId) {
    console.log('Please provide a Movie ID as the first argument.');
    process.exit(1);
  }
  
  // Define the URL for the Star Wars API films endpoint
  const filmsUrl = 'https://swapi.dev/api/films/';
  
  // Function to fetch the character data for a specific movie
  function getCharactersForMovie(movieId) {
    // Make a request to the films endpoint to get film data
    request(filmsUrl, { json: true }, (error, response, body) => {
      if (error) {
        console.error('Error fetching data:', error);
        return;
      }
  
      // Find the movie with the specified ID
      const movie = body.results.find((film) => film.episode_id == movieId);
  
      if (!movie) {
        console.log(`Movie with ID ${movieId} not found.`);
        return;
      }
  
      // Fetch and print the characters in the same order as the "characters" list
      movie.characters.forEach((characterUrl) => {
        request(characterUrl, { json: true }, (error, response, characterData) => {
          if (error) {
            console.error('Error fetching character data:', error);
            return;
          }
  
          console.log(characterData.name);
        });
      });
    });
  }
  
  // Call the function to fetch characters for the specified movie
  getCharactersForMovie(movieId);
  