import {
  GraphQLObjectType,
  GraphQLSchema,
  GraphQLList,
  GraphQLID,
  GraphQLString,
  GraphQLInt,
  GraphQLBoolean,
  GraphQLNonNull
} from 'graphql';
import models from './models';

const UserType = new GraphQLObjectType({
  name: 'user',
  fields: () => ({
    id: { type: GraphQLID },
    username: { type: GraphQLString },
    amount: { type: GraphQLInt },
    total: { type: GraphQLInt },
  }),
});

const ChannelType = new GraphQLObjectType({
  name: 'channel',
  fields: () => ({
    id: { type: GraphQLID },
    channelname: { type: GraphQLString },
    enabled: { type: GraphQLBoolean },
    points: { type: new GraphQLList(UserType) },
  }),
});

const CommandBodyType = new GraphQLObjectType({
  name: 'commandBody',
  fields: () => ({
    message: { type: GraphQLString },
    options: { type: new GraphQLList(GraphQLString) },
    fnName: { type: GraphQLString },
    timing: { type: GraphQLInt },
  }),
});

const CommandType = new GraphQLObjectType({
  name: 'command',
  fields: () => ({
    id: { type: GraphQLID },
    name: { type: GraphQLString },
    type: { type: GraphQLString },
    body: { type: CommandBodyType },
    description: { type: GraphQLString },
    timeout: { type: GraphQLInt },
    availableOnAllChannels: { type: GraphQLBoolean },
    channels: { type: new GraphQLList(ChannelType) },
  }),
});

const Query = new GraphQLObjectType({
  name: 'Query',
  fields: () => ({
    command: {
      type: CommandType,
      args: { name: { type: GraphQLString } },
      resolve: (parent, args) => models.Command.findOne({ name: args.name.toLowerCase() }),
    },
    channelCommands: {
      type: new GraphQLList(CommandType),
      args: { channel: { type: GraphQLString } },
      resolve: (parent, args) => models.Command.findOne({ 'channels.name': args.channel.toLowerCase() })
    },
    commands: {
      type: new GraphQLList(CommandType),
      resolve: () => models.Command.find({}),
    }
  }),
});

const Mutation = new GraphQLObjectType({
  name: 'Mutation',
  fields: () => ({
    addCommand: {
      type: CommandType,
      args: {
        name: { type: new GraphQLNonNull(GraphQLString) },
        type: { type: new GraphQLNonNull(GraphQLString) },
        description: { type: GraphQLString },
        body: { type: CommandBodyType },
        timeout: { type: GraphQLInt },
      },
      resolve: (parent, args) => {
        const newCommand = new models.Command(args);
        return newCommand.save();
      },
    },
    updateCommand: {
      type: CommandType,
      args: {
      },
      resolve: (parent, args) => models.Command.findOneAndUpdate({ id: args.id }, args),
    },
  }),
});

export default new GraphQLSchema({
  query: Query,
  mutation: Mutation,
});
