const mongoose = require('mongoose');

mongoose.connect(process.env.DATABASE_URL);

const Stream = mongoose.model('Stream', {
  streamId: String,
  userId: String,
  username: String,
  gameId: String,
  title: String,
  startedAt: String
});

module.exports = {
  Stream
};
