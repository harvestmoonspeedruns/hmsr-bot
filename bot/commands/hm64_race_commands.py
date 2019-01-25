from bot.commands import BaseCommands


class HM64RaceCommands(BaseCommands):
    betting_open = False
    bets = {}

    def __init__(self):
        self.commands = {
            "startrace": {
                "kwargs": ["startrace", "startbetting"],
                "func": self.start_race,
                "docs": "Starts a new race, will erase existing bets and open new betting.",
            },
            "endrace": {
                "kwargs": ["endrace", "endbetting"],
                "func": self.end_race,
                "docs": "Closes the race and no new bets are allowed.",
            },
            "bet": {
                "kwargs": ["bet", "dog", "horse"],
                "func": self.bet,
                "docs": "Places a bet for that user with whatever number following command. Only 1 bet per user.",
            },
            "winner": {
                "kwargs": ["winner", "winners"],
                "func": self.winner,
                "docs": "Announces all bets who matched the number following command",
            },
        }

    def start_race(self, event, channel):
        actor, arguments, is_mod = self.get_event_variables(event)
        if not is_mod:
            return

        self.bets = {}
        self.betting_open = True
        return "Betting is now open. Good Luck! FrankerZ vs OhMyDog vs RalpherZ vs BegWan vs ChefFrank vs CorgiDerp"

    def end_race(self, event, channel):
        actor, arguments, is_mod = self.get_event_variables(event)
        if not is_mod:
            return

        self.betting_open = True
        return "Betting is now closed!"

    def bet(self, event, channel):
        actor, arguments, is_mod = self.get_event_variables(event)
        if self.betting_open and actor not in self.bets and len(arguments) >= 2:
            self.bets[actor] = arguments[1]

    def winner(self, event, channel):
        actor, arguments, is_mod = self.get_event_variables(event)
        if not is_mod:
            return

        winners = []
        for (user, bet) in self.bets.items():
            if len(arguments) >= 2 and bet == arguments[1]:
                winners.append("@" + user)

        congrats_to = "all"
        if len(winners) == 0:
            winners.append("a myth")
            winners.append("BibleThump")
            congrats_to = "no one"
        elif len(winners) == 1:
            congrats_to = "you"

        return "Winners are {0}. Congrats to {1}!".format(
            " ".join(winners), congrats_to
        )
