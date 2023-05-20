import json
import readline
import time

from pynput import keyboard, mouse
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController

keyDictionary = {
    "Key.alt": Key.alt,
    "Key.alt_l": Key.alt_l,
    "Key.alt_r": Key.alt_r,
    "Key.alt_gr": Key.alt_gr,
    "Key.backspace": Key.backspace,
    "Key.caps_lock": Key.caps_lock,
    "Key.cmd": Key.cmd,
    "Key.cmd_l": Key.cmd_l,
    "Key.cmd_r": Key.cmd_r,
    "Key.ctrl": Key.ctrl,
    "Key.ctrl_l": Key.ctrl_l,
    "Key.ctrl_r": Key.ctrl_r,
    "Key.delete": Key.delete,
    "Key.down": Key.down,
    "Key.end": Key.end,
    "Key.enter": Key.enter,
    "Key.esc": Key.esc,
    "Key.f1": Key.f1,
    "Key.f2": Key.f2,
    "Key.f3": Key.f3,
    "Key.f4": Key.f4,
    "Key.f5": Key.f5,
    "Key.f6": Key.f6,
    "Key.f7": Key.f7,
    "Key.f8": Key.f8,
    "Key.f9": Key.f9,
    "Key.f10": Key.f10,
    "Key.f11": Key.f11,
    "Key.f12": Key.f12,
    "Key.f13": Key.f13,
    "Key.f14": Key.f14,
    "Key.f15": Key.f15,
    "Key.f16": Key.f16,
    "Key.f17": Key.f17,
    "Key.f18": Key.f18,
    "Key.f19": Key.f19,
    "Key.f20": Key.f20,
    "Key.home": Key.home,
    "Key.left": Key.left,
    "Key.page_down": Key.page_down,
    "Key.page_up": Key.page_up,
    "Key.right": Key.right,
    "Key.shift": Key.shift,
    "Key.shift_l": Key.shift_l,
    "Key.shift_r": Key.shift_r,
    "Key.space": Key.space,
    "Key.tab": Key.tab,
    "Key.up": Key.up,
    "Key.media_play_pause": Key.media_play_pause,
    "Key.media_volume_mute": Key.media_volume_mute,
    "Key.media_volume_down": Key.media_volume_down,
    "Key.media_volume_up": Key.media_volume_up,
    "Key.media_previous": Key.media_previous,
    "Key.media_next": Key.media_next,
    "Key.insert": Key.insert,
    "Key.menu": Key.menu,
    "Key.num_lock": Key.num_lock,
    "Key.pause": Key.pause,
    "Key.print_screen": Key.print_screen,
    "Key.scroll_lock": Key.scroll_lock}

keyring = keyDictionary.keys()
valuering = keyDictionary.values()

keyboard = KeyboardController()
mouse = MouseController()


def replay_events(click_speed = 0.5,mouse_speed = 0.02):
    # Read the events from the file
    with open("events.txt", "r") as f:
        events = json.load(f)

    for event in events:
        if event[0] == "s":  # Keyboard press event
            time.sleep(click_speed)
            
            if isinstance(event[1], str):  # Character key
                keyboard.press(Key[event[1].split('.')[1]])
                keyboard.release(Key[event[1].split('.')[1]])

        # elif event[0] == "k":  # Press character key
        #     time.sleep(click_speed)
        #     if isinstance(event[1], str):  # Character key
        #         key_event = event[1].split('+')[0].strip()
        #         if 'Key' in key_event:
        #             char_event = event[1].split('+')[1].strip().replace("'", "")
        #             if char_event in keyring:
        #                 keyboard.press(Key[key_event.split('.')[1]]) #press Key.alt
        #                 keyboard.press(Key[char_event.split('.')[1]])# press Key.f2
        #                 keyboard.release(Key[char_event.split('.')[1]])
        #                 keyboard.release(Key[key_event.split('.')[1]])
        #             else:
        #                 keyboard.press(Key[key_event.split('.')[1]])
        #                 keyboard.press(KeyCode(char=char_event))
        #                 keyboard.release(KeyCode(char=char_event))
        #                 keyboard.release(Key[key_event.split('.')[1]])
        #         else:
        #             keyboard.press(event[1])
        #             keyboard.release(event[1])
        
        elif event[0] == "k":  # Press character key
            time.sleep(mouse_speed)
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
            time.sleep(mouse_speed)
            mouse.position = (event[1], event[2])

        elif event[0] == "c":  # Mouse click event
            time.sleep(click_speed)
            if event[3] == "Button.left":
                mouse.position = (event[1], event[2])
                mouse.click(Button.left)
            elif event[3] == "Button.right":
                mouse.position = (event[1], event[2])
                mouse.click(Button.right)
