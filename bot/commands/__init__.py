class BaseCommands(object):
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
        return actor, arguments
