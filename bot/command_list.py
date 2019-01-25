from bot.commands.hm64_race_commands import HM64RaceCommands
from bot.commands.hm64_all_photos_info import HM64AllPhotosInfo
from bot.commands.pastor_brown_commands import PastorBrownCommands
from bot.commands.reminder_commands import ReminderCommands


class CommandList(object):
    _command_cls = [HM64RaceCommands, HM64AllPhotosInfo, PastorBrownCommands, ReminderCommands]

    def __init__(self):
        self.commands = {}
        self.commandDefinitions = {}
        classes = [Class() for Class in self._command_cls]
        for commands in classes:
            commands.register(self)
