import datetime

from bot.commands import BaseCommands


class ReminderCommands(BaseCommands):
    def __init__(self):
        self.commands = {
            "start_reminder": {
                "docs": "starts reminder with the command name as parameter",
                "func": self.start_reminder,
            },
            "say_reminders": {
                "func": self.say_reminders,
            },
            "stop_reminder": {
                "docs": "ends reminder with the command name as parameter",
                "func": self.end_reminder,
            },
            "save10": {
                "kwargs": [],
                "reminder": True,
                "docs": "reminder to save every 10 minutes",
                "timer": 10 * 60,
                "func": self.reminder_message("save10", "/me [reminder] It's been 10 minutes. You should save!"),
            },
            "save30": {
                "kwargs": [],
                "reminder": True,
                "docs": "reminder to save every 30 minutes",
                "timer": 30 * 60,
                "func": self.reminder_message("save30", "/me [reminder] It's been 30 minutes. You should save!"),
            },
            "save60": {
                "kwargs": [],
                "reminder": True,
                "docs": "reminder to save every 60 minutes",
                "timer": 60 * 60,
                "func": self.reminder_message("save60", "/me [reminder] It's been 60 minutes. You should save!"),
            },
        }
