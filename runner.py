'''
Copyright 2019 Blake Grotewold <hello@grote.world>

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
'''

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