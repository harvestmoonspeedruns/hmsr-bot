const fetch = require('node-fetch');
require('dotenv').config();

const args = process.argv.slice(2);

if (args.length < 1) process.exit(1); // Don't go further

const options = { headers: { 'Client-Id': process.env.TWITCH_CLIENT_ID } };
fetch(`https://api.twitch.tv/helix/games?name=${args[0]}`, options)
  .then(res => res.json())
  .then(game => console.log(game));
