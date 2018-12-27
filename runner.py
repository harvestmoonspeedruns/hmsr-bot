import os
import sys

from bot.pastor_brown import PastorBrown

def main():
    username = "pastor_brown"
    client_id = os.environ.get("CLIENT_ID")
    token = os.environ.get("TOKEN")
    channels = os.environ.get("CHANNELS").split(",")

    bots = {}
    for channel in channels:
        bots[channel] = PastorBrown(username, client_id, token, channel)
        bots[channel].start()

if __name__ == "__main__":
    main()