class BaseCommands(object):
    def register(self, list):
        for command in self.commands.values():
            for keyword in command.get("kwargs"):
                list.commands[keyword] = command.get("func")

    @staticmethod
    def get_event_variables(event):
        actor = event.source.split("!")[0]
        arguments = event.arguments[0].split(" ")
        return actor, arguments
