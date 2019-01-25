from threading import Timer

class BaseCommands(object):
    is_stop = {}
    output = []

    def register(self, list):
        for title, command in self.commands.items():
            for keyword in command.get("kwargs", [title]):
                list.commands[keyword] = command.get("func")
                if command.get("docs"):
                    list.commandDefinitions[keyword] = command.get("docs")

    @staticmethod
    def get_event_variables(event):
        actor = event.source.split("!")[0]
        arguments = event.arguments[0].split(" ")
        badges = next(tag["value"] for tag in event.tags if tag["key"] == "badges")
        is_mod = (
            badges and ("broadcaster" in badges or "moderator" in badges or actor == "groteworld")
        )
        return actor, arguments, is_mod

    def messageReturner(self, message):
        return lambda e, c: message.replace("\n", " ")

    def start_reminder(self, event, channel):

        actor, arguments, is_mod = self.get_event_variables(event)
        reminder_name = None
        if len(arguments) >= 2:
            reminder_name = arguments[1]

        if not reminder_name or not self.commands[reminder_name].get("reminder"):
            return "No reminder with name {}".format(reminder_name)
        self.is_stop[reminder_name] = False
        BaseCommands.setInterval(
            self.commands[reminder_name].get("timing"),
            self.commands[reminder_name].get("func"))
        print("Starting Reminder: {}".format(reminder_name))

    def end_reminder(self, event, channel):
        actor, arguments, is_mod = self.get_event_variables(event)
        if len(arguments) >= 2:
            reminder_name = arguments[1]

        if not reminder_name:
            return
        self.is_stop[reminder_name] = True

        print("Stopping Reminder: {}".format(reminder_name))

    def reminder_message(self, task_name, message):
        return lambda: self.output.append(message) if not self.is_stop.get(task_name, True) else True

    def say_reminders(self):
        if len(self.output) > 0:
            return self.output.pop()

    @staticmethod
    def setInterval(timer, task):
        is_stop = task()
        if not is_stop == True:
            Timer(timer, BaseCommands.setInterval, [timer, task]).start()
