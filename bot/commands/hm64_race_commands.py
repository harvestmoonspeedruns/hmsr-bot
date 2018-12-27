from bot.commands import BaseCommands

class HM64RaceCommands(BaseCommands):
    betting_open = False
    bets = {}

    def __init__(self):
        self.commands = {
            "startrace": {
                "kwargs": ["startrace", "startbetting"],
                "func": self.start_race
            },
            "endrace": {
                "kwargs": ["endrace", "endbetting"],
                "func": self.end_race
            },
            "bet": {
                "kwargs": ["bet", "dog", "horse"],
                "func": self.bet
            },
            "winner": {
                "kwargs": ["winner", "winners"],
                "func": self.winner
            }
        }

    def start_race(self, event, channel):
        self.bets = {}
        self.betting_open = True
        return "Betting is now open. Good Luck! OhMyDog"


    def end_race(self, event, channel):
        self.betting_open = True
        return "Betting is now closed!"

    def bet(self, event, channel):
        actor, arguments = self.get_event_variables(event)
        if self.betting_open and actor not in self.bets and len(arguments) >= 2:
            self.bets[actor] = arguments[1]

    def winner(self, event, channel):
        actor, arguments = self.get_event_variables(event)
        winners = []
        for (user, bet) in self.bets.items():
            if len(arguments) >= 2 and bet == arguments[1]:
                winners.append("@"+user)

        congrats_to = "all"
        if len(winners) == 0:
            winners.append("a myth")
            winners.append("BibleThump")
            congrats_to = "no one"
        elif len(winners) == 1:
            congrats_to = "you"

        return "Winners are {0}. Congrats to {1}!".format(" ".join(winners), congrats_to)
