import json
import threading
import time
import datetime

from pynput.keyboard import Key, Controller, Listener as KeyboardListener
from pynput.mouse import Button, Listener as MouseListener
class CustomButton:
    def __init__(self, label, style):
        self.label = label
        self.style = style

    def to_dict(self):
        return {
            'name': self.label,
            'x': self.style,
            'y': self.style,
            'button': self.style,
        }

class ButtonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, CustomButton):
            return obj.to_dict()
        return super().default(obj)

def record():
    global start_time
    start_time = datetime.datetime.now()
    # Define a list to store the events
    events = []

    # Define a set to keep track of pressed modifier keys
    modifier_keys = set()
    
    

    def on_press(key):
        nonlocal modifier_keys
        global start_time

        mod_keys = [Key.ctrl, Key.shift, Key.alt]

        # Calculate the timestamp since the start of recording
        timestamp = datetime.datetime.now() - start_time

        # Wait for a specific key combination to be pressed to stop recording
        if key == Key.esc:
            # Stop the listeners
            keyboard_listener.stop()
            mouse_listener.stop()
            
            # Write the events to a file
            with open("events.txt", "w") as f:
                json.dump(events, f, cls=ButtonEncoder)
                
                
            print("Stop recording...Saving file, please wait...")
            return False

        # Handle modifier keys (Ctrl, Shift, Alt)
        if key in mod_keys:
            modifier_keys.add(key)
            return

        # Check if any modifier keys are pressed
        if modifier_keys:
            # Combine the modifier keys with the current key
            key_combination = ' + '.join([str(modifier) for modifier in modifier_keys]) + ' + ' + str(key)
            events.append(("k", key_combination, timestamp.total_seconds()))
            
            # restart the timer for the next key
            start_time = datetime.datetime.now()
            # Remove released modifier keys from the set
            if key not in mod_keys:
                for key in mod_keys:
                    modifier_keys.discard(key)
        else:
            try:
                events.append(("k", key.char, timestamp.total_seconds()))
                # restart the timer for the next key
                start_time = datetime.datetime.now()
            except AttributeError:
                # Convert non-literal values to strings
                events.append(("s", str(key), timestamp.total_seconds()))
                # restart the timer for the next key
                start_time = datetime.datetime.now()


    # Define a function to handle mouse events
    def on_move(x, y):
        global start_time
        
        # Calculate the timestamp since the start of recording
        timestamp = datetime.datetime.now() - start_time

        events.append(("m", x, y, timestamp.total_seconds()))
        # restart the timer for the next key
        start_time = datetime.datetime.now()

    def on_click(x, y, button, pressed):
        global start_time
        
        if pressed:
            # Calculate the timestamp since the start of recording
            timestamp = datetime.datetime.now() - start_time

            events.append(("c", x, y, str(button), timestamp.total_seconds()))
            # restart the timer for the next key
            start_time = datetime.datetime.now()

    def on_scroll(x, y, dx, dy):
        global start_time
        # Calculate the timestamp since the start of recording
        timestamp = datetime.datetime.now() - start_time

        events.append(("sc", x, y, dx, dy, timestamp.total_seconds()))
        # restart the timer for the next key
        start_time = datetime.datetime.now()

    # Create the listener objects
    keyboard_listener = KeyboardListener(on_press=on_press)
    mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

    # Start the listeners
    keyboard_listener.start()
    mouse_listener.start()

    keyboard_listener.join()
    mouse_listener.join()
    print("End of recording...")
