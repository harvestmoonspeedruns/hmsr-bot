"""
Copyright 2019 Blake Grotewold <hello@grote.world>

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
"""

from bot.twitch import TwitchBot
from bot.command_list import CommandList


class PastorBrown(TwitchBot):
    def __init__(self, username, client_id, token, channel):
        super().__init__(username, client_id, token, channel)
        self.command_list = CommandList()

    def do_command(self, e, cmd):
        if cmd in self.command_list.commands.keys():
            message = self.command_list.commands[cmd](e, self.channel)
            if message:
                self.send(message)
