from bot.commands import BaseCommands


class PastorBrownCommands(BaseCommands):
    def __init__(self):
        self.commands = {
            "help": {
                "docs": "Helpful command for commands",
                "kwargs": ["help", "pastor_brown", "commands"],
                "func": self.messageReturner("https://github.com/groteworld/pastor_brown/blob/master/COMMANDS.md"),
            },
            "mips": {
                "docs": "Explaination about MIPS Chip",
                "func": self.messageReturner("The MIPS chip is the CPU of the Nintendo 64. In HM64, numbers are saved into short storage of the CPU which causes RNG to be similar between runs, unless the console is turned off and the batteries on the CPU run out of power."),
            },
            "oddtom": {
                "docs": "what is oddtommin?",
                "kwargs": ["oddtomming", "oddtom"],
                "func": self.messageReturner("An OddTom is a common mistake made in all photos runs, like sleeping through the dog race, or not getting your wife pregnant. overall, pretty disappointing Kappa"),
            },
            "gddto": {
                "docs": "what is oddtommin?",
                "kwargs": ["godtomming", "godtom"],
                "func": self.messageReturner("A GodTom is a rare, and beautiful occurance of luck, like first try coin, or getting farm berry. overall, pretty cool Kappa"),
            },
        }
