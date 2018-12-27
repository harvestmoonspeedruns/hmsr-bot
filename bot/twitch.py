"""
Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
Copyright 2019 Blake Grotewold <hello@grote.world>

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
"""

import sys
import requests
from irc.bot import SingleServerIRCBot


class TwitchBot(SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = "#" + channel

        # Get the channel id, we will need this for API calls
        url = "https://api.twitch.tv/helix/users?login=" + channel
        headers = {"Client-ID": client_id}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r["data"][0]["id"]

        # Create IRC bot connection
        server = "irc.chat.twitch.tv"
        port = 6667
        print("Connecting to " + server + " on port " + str(port) + "...")
        SingleServerIRCBot.__init__(
            self, [(server, port, "oauth:" + token)], username, username
        )

    def on_welcome(self, c, e):
        print("Joining " + self.channel)

        # You must request specific capabilities before you can use them
        c.cap("REQ", ":twitch.tv/membership")
        c.cap("REQ", ":twitch.tv/tags")
        c.cap("REQ", ":twitch.tv/commands")
        c.join(self.channel)

    def on_pubmsg(self, c, e):

        # If a chat message starts with an exclamation point, try to run it as a command
        if e.arguments[0][:1] == "+":
            cmd = e.arguments[0].split(" ")[0][1:].lower()
            print("Received command:", self.channel, cmd)
            self.do_command(e, cmd)
        return

    def send(self, message):
        self.connection.privmsg(self.channel, message)
