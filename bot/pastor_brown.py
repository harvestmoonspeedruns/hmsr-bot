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

            self.send("Winners are {0}. Congrats to {1}!".format(" ".join(winners), congrats_to))
