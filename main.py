from recorder import record
from play_macro import replay_events
from time import sleep
import os
import datetime

# start = datetime.datetime.now()
# sleep(2)
# now = datetime.datetime.now()
# stop = now - start
# print(stop.total_seconds())


# exit()

def counter():
    print("\n3...\n")
    sleep(1)
    print("\n2...\n")
    sleep(1)
    print("\n1...\n")
    sleep(1)

options = ["1. Record", "2. Play", "3. Exit"]
os.system("clear")
while True:
    # os.system("clear")
    for option in options:
        print(option)
    answer = input(f"\nChoose from 1-{len(options)}\n")
    if str(answer) == "1":
        counter()
        print("\nRecording...\n")
        record()
        continue
    elif str(answer) == "2":
        counter()
        print("\nPlaying...\n")
        print("\nEsc button to 'Stop'\n\nPlaying...\n")
        replay_events()
        print("\nStopped playing...\n")
        continue
    else:
        print("\nEnd of program!\n")
        break