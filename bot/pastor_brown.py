"""
Copyright 2019 Blake Grotewold <hello@grote.world>

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
"""

import datetime
from threading import Timer

from bot.twitch import TwitchBot
from bot.command_list import CommandList


class PastorBrown(TwitchBot):
    def __init__(self, username, client_id, token, channel):
        super().__init__(username, client_id, token, channel)
        self.command_list = CommandList()
        self.previousCommands = {}

        PastorBrown.setInterval(60, self.check_for_reminders)

    @staticmethod
    def setInterval(timer, task):
        task()
        Timer(timer, PastorBrown.setInterval, [timer, task]).start()

    def check_for_reminders(self):
        message = self.command_list.commands.get("say_reminders")()
        if message: self.send(message)

    def do_command(self, e, cmd):
        if cmd in self.command_list.commands.keys() and (
            cmd not in self.previousCommands
            or datetime.datetime.now() > self.previousCommands[cmd]
        ):
            message = self.command_list.commands[cmd](e, self.channel)
            if message:
                self.previousCommands[
                    cmd
                ] = datetime.datetime.now() + datetime.timedelta(0, 10)
                self.send(message)
