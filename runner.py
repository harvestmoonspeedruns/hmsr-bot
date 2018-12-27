import os
import sys
from multiprocessing import Process

from bot.pastor_brown import PastorBrown

def main():
    username = "pastor_brown"
    client_id = os.environ.get("CLIENT_ID")
    token = os.environ.get("TOKEN")
    channels = os.environ.get("CHANNELS").split(",")

    bots = {}
    processes = []
    for channel in channels:
        bots[channel] = PastorBrown(username, client_id, token, channel)
        process = Process(target=bots[channel].start)
        processes.append(process)
        process.start()



if __name__ == "__main__":
    main()