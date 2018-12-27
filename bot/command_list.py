from bot.commands.hm64_race_commands import HM64RaceCommands


class CommandList(object):
    _command_cls = [HM64RaceCommands]


    def __init__(self):
        self.commands = {}
        classes = [Class() for Class in self._command_cls]
        for commands in classes:
            commands.register(self)