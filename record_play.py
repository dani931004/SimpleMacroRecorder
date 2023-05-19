import time
import json
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Button, Listener as MouseListener
from pynput import mouse

keyboard = KeyboardController()
mouse = MouseController()
# This code is made with the cooperation of GPT =) not my code xD
class Button:
    def __init__(self, label, style):
        self.label = label
        self.style = style
    
    def to_dict(self):
        return {
            'name': self.label,
            'key': self.style,
        }

class ButtonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Button):
            return obj.to_dict()
        return super().default(obj)

def record():
    # Define a list to store the events
    events = []

    # Define a function to handle keyboard events
    def on_press(key):
        # Wait for a specific key to be pressed to stop recording
        if key == Key.esc:
            # Stop the listener
            return False
        try:
            events.append(("k", key.char))
        except AttributeError:
            events.append(("s", str(key)))  # Convert non-literal values to strings

    # Define a function to handle mouse events
    def on_move(x, y):
        events.append(("m", x, y))

    def on_click(x, y, button, pressed):
        if pressed:
            events.append(("c", x, y, button))

    # Create the listener objects
    keyboard_listener = KeyboardListener(on_press=on_press)
    mouse_listener = MouseListener(on_move=on_move, on_click=on_click)

    # Start the listeners
    keyboard_listener.start()
    mouse_listener.start()
    print("Started listening")
    time.sleep(10)

    # Stop the listeners
    keyboard_listener.stop()
    mouse_listener.stop()
    print("Stopped listening")
    # Write the events to a file
    with open("events.txt", "w") as f:
        json.dump(events, f, cls=ButtonEncoder)



def replay_events():
    # Read the events from the file
    with open("events.txt", "r") as f:
        events = json.load(f)

    for event in events:
        time.sleep(1)
        if event[0] == "s":  # Keyboard event
            if isinstance(event[1], str):  # Character key
                keyboard.press(Key[event[1].split('.')[1]])
                keyboard.release(Key[event[1].split('.')[1]])
            else:  # Special key
                if event[1] == "alt":
                    keyboard.press(Key.alt)
                    keyboard.release(Key.alt)
                else:
                    keyboard.press(Key[event[1].split('.')[1]])
                    keyboard.release(Key[event[1].split('.')[1]])
        elif event[0] == "m":  # Mouse movement event
            mouse.position = (event[1], event[2])
        elif event[0] == "c":  # Mouse click event
            if event[3] == mouse.Button.left:
                mouse.position = (event[1], event[2])
                mouse.click(mouse.Button.left)
            elif event[3] == mouse.Button.right:
                mouse.position = (event[1], event[2])
                mouse.click(mouse.Button.right)


# print("Recording...")
# record()
# print("Stopped recording...")
# time.sleep(3)

# Wait for a few seconds before replaying the events
# print("Start replaying... in 3 seconds")
# time.sleep(3)

# Replay the events
print("Replaying...")
replay_events()
