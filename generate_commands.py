from bot.command_list import CommandList

def main():
    command_list = CommandList()

    with open("COMMANDS.md", "w") as command_file:
        print("# Commands", file=command_file)
        print("", file=command_file)
        print("All commands start with `+` symbol and are case-insensitive.", file=command_file)
        print("", file=command_file)

        for cmd in sorted(command_list.commandDefinitions):
            print("`+{0}`: {1}".format(cmd, command_list.commandDefinitions[cmd]), file=command_file, end="  \n")

if __name__ == "__main__":
    main()