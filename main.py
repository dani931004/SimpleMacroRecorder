from recorder import play_recorder
from play_macro import play
from time import sleep
import os


options = ["1. Record", "2. Play", "3. Exit"]
os.system("clear")
while True:
    # os.system("clear")
    print("\n")
    for option in options:
        print(option)
    answer = input(f"\nChoose from 1-{len(options)}\n")
    if str(answer) == "1":
        print("\nRecording...\n")
        play_recorder()
        continue
    elif str(answer) == "2":
        print("\nPlaying...\n")
        print("\nMouse to upper left corner to 'Stop'\n\nPlaying...\n")
        play()
        continue
    else:
        print("\nEnd of program!\n")
        break