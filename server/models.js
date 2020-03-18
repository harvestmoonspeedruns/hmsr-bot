import mongoose from 'mongoose';

require('dotenv').config();

mongoose.connect(process.env.DATABASE_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

mongoose.ObjectId.prototype.valueOf = () => this.toString();

mongoose.connection.once('open', () => {
  console.log('connected to database');
});


const UserSchema = new mongoose.Schema({
  id: String, // TwitchID
  username: String,
  amount: Number,
  total: Number,
});

const ChannelSchema = new mongoose.Schema({
  id: String, // TwitchID
  name: String,
  points: [UserSchema],
  enabled: Boolean,
});

const CommandBodySchema = new mongoose.Schema({
  message: String,
  options: [String],
  fnName: String,
  timing: Number,
});

const CommandSchema = new mongoose.Schema({
  id: mongoose.Schema.Types.ObjectId,
  name: String,
  type: String,
  body: CommandBodySchema,
  description: String,
  timeout: Number,
  availableOnAllChannels: Boolean,
  channels: [ChannelSchema],
});

export default {
  Command: mongoose.model('Command', CommandSchema),
  CommandBody: mongoose.model('CommandBody', CommandBodySchema),
  Channel: mongoose.model('Channel', ChannelSchema),
  User: mongoose.model('User', UserSchema),
};
