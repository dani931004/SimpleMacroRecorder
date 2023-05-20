from recorder import record
from play_macro import replay_events
from time import sleep
import os

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
        print("\nMouse to upper left corner to 'Stop'\n\nPlaying...\n")
        replay_events()
        continue
    else:
        print("\nEnd of program!\n")
        break