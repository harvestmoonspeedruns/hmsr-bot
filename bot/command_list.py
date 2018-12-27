from bot.commands.hm64_race_commands import HM64RaceCommands
from bot.commands.hm64_all_photos_info import HM64AllPhotosInfo


class CommandList(object):
    _command_cls = [HM64RaceCommands, HM64AllPhotosInfo]

    def __init__(self):
        self.commands = {}
        classes = [Class() for Class in self._command_cls]
        for commands in classes:
            commands.register(self)