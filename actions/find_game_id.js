const fetch = require('node-fetch');
require('dotenv').config();

const args = process.argv.slice(2);

if (args.length < 1) process.exit(1); // Don't go further

const authOptions = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  }
};
const authQueryString = `?client_id=${process.env.TWITCH_CLIENT_ID}&client_secret=${process.env.TWITCH_CLIENT_SECRET}&grant_type=client_credentials`;
const twitchAuthEndpoint = `https://id.twitch.tv/oauth2/token${authQueryString}`;

fetch(twitchAuthEndpoint, authOptions).then(res => res.json()).then((auth) => {
  const options = { headers: { Authorization: `Bearer ${auth.access_token}`, 'Client-Id': process.env.TWITCH_CLIENT_ID } };

  fetch(`https://api.twitch.tv/helix/games?name=${args[0]}`, options)
    .then(res => res.json())
    .then(game => console.log(game));
});
