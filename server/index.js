import express from 'express';
import graphqlHTTP from 'express-graphql';
import Bundler from 'parcel-bundler';
import schema from './schema';
import middleware from './middleware';

require('dotenv').config();

const reactFile = 'index.html'; // Pass an absolute path to the entrypoint here
const reactOptions = {}; // See options section of api docs, for the possibilities

const app = express();

console.log('Running a GraphQL API server at http://localhost:4000/graphql');

app.use(middleware.auth);

app.use(
  '/graphql',
  graphqlHTTP({
    schema,
    graphiql: false,
  }),
);

// Let express use the bundler middleware,
// this will let Parcel handle every request over your express server
const bundler = new Bundler(reactFile, reactOptions);
app.use(bundler.middleware());

app.listen(4000);
