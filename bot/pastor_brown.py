'''
Copyright 2019 Blake Grotewold <hello@grote.world>

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
'''

from bot.twitch import TwitchBot

class PastorBrown(TwitchBot):
    bets = {}
    betting_open = False

    def __init__(self, username, client_id, token, channel):
        super().__init__(username, client_id, token, channel)


    def do_command(self, e, cmd):
        actor = e.source.split("!")[0]
        arguments = e.arguments[0].split(" ")

        if cmd in ["dog", "horse", "bet"]:
            if self.betting_open and actor not in self.bets and len(arguments) >= 2:
                self.bets[actor] = arguments[1]

        elif cmd == "startrace":
            self.bets = {}
            self.betting_open = True
            self.send("Betting is now open. Good Luck! OhMyDog")

        elif cmd == "endbetting":
            self.betting_open = True
            self.send("Betting is now closed!")

        elif cmd == "winners":
            winners = []
            for (user, bet) in self.bets.items():
                if len(arguments) >= 2 and bet == arguments[1]:
                    winners.append(user)

            congrats_to = "all"
            if len(winners) == 0:
                winners.append("a myth")
                winners.append("BibleThump")
                congrats_to = "no one"
            elif len(winners) == 1:
                congrats_to = "you"

            self.send("Winners are {0}. Congrats to {1}!".format(" @".join(winners), congrats_to))
