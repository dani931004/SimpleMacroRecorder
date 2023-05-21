import json
import time

from pynput import keyboard, mouse
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key, KeyCode
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

stop_flag = False  # Flag to indicate if the program should stop

normal_speed = True # Flag to indicate what is the speed of replaying

def on_press(key):
    global stop_flag
    if key == Key.esc:
        stop_flag = True  # Set the stop flag when Esc key is pressed


def replay_events():
    # Read the events from the file
    with open("events.txt", "r") as f:
        events = json.load(f)

    # Create and start the listener for the Esc key
    listener = KeyboardListener(on_press=on_press)
    listener.start()

    for event in events:
        if stop_flag:  # Check the stop flag before processing each event
            break

        if event[0] == "s":  # Keyboard press event
            if normal_speed: # Normal speed
                time.sleep(float(event[2]))

            if isinstance(event[1], str):  # Character key
                keyboard.press(Key[event[1].split('.')[1]])
                keyboard.release(Key[event[1].split('.')[1]])

        elif event[0] == "k":  # Press character key
            time.sleep(float(event[2]))
            if isinstance(event[1], str):  # Character key
                key_combination = event[1].split('+')  # Split the keys by '+'
                keys_to_press = []

                for key in key_combination:
                    key = key.strip()  # Remove whitespace
                    if 'Key' in key:
                        keys_to_press.append(key)
                    else:
                        keys_to_press.append(key.replace("'", ""))

                for key in keys_to_press:
                    if 'Key' in str(key):
                        keyboard.press(Key[key.split('.')[1]])
                    else:
                        keyboard.press(KeyCode(char=key.replace('"', '')))

                for key in reversed(keys_to_press):
                    if 'Key' in str(key):
                        keyboard.release(Key[key.split('.')[1]])
                    else:
                        keyboard.release(KeyCode(char=key.replace('"', '')))

        elif event[0] == "m":  # Mouse movement event
            time.sleep(event[3])
            mouse.position = (event[1], event[2])

        elif event[0] == "sc":  # Mouse movement event
            time.sleep(event[5])
            mouse.position = (event[1], event[2])
            dx, dy = event[3], event[4]
            mouse.scroll(dx, dy)

        elif event[0] == "c":  # Mouse click event
            time.sleep(event[4])
            if event[3] == "Button.left":
                mouse.position = (event[1], event[2])
                mouse.click(Button.left)
            elif event[3] == "Button.right":
                mouse.position = (event[1], event[2])
                mouse.click(Button.right)

    listener.stop()  # Stop the listener after all events are processed
