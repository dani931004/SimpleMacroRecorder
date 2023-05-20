import json
from pynput.keyboard import Key, Listener as KeyboardListener
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
    # Define a list to store the events
    events = []

    # Define a function to handle keyboard events
    # def on_press(key):
    #     # Wait for a specific key to be pressed to stop recording
    #     print("Key pressed", key)
    #     if key == Key.esc:
    #         # Stop the listeners
    #         keyboard_listener.stop()
    #         mouse_listener.stop()
    #         print("Stopped listening")
    #         # Write the events to a file
    #         with open("events.txt", "w") as f:
    #             json.dump(events, f, cls=ButtonEncoder)

    #     try:
    #         events.append(("k", key.char))
    #     except AttributeError:
    #         # Convert non-literal values to strings
    #         events.append(("s", str(key)))

    pressed_keys = set()

    def on_press(key):
        # Add the pressed key to the set of pressed keys
        print("Key pressed", key)
        # Wait for a specific key combination to be pressed to stop recording
        if key == Key.esc:
            print("Stopping recording...")
            # Stop the listeners
            keyboard_listener.stop()
            mouse_listener.stop()
            print("Stopped listening")

        try:
            events.append(("k", key.char))
        except AttributeError:
            # Convert non-literal values to strings
            events.append(("s", str(key)))

        # Write the events to a file
        with open("events.txt", "w") as f:
            json.dump(events, f, cls=ButtonEncoder)

    # Define a function to handle mouse events
    def on_move(x, y):
        events.append(("m", x, y))

    def on_click(x, y, button, pressed):
        if pressed:
            print(button)
            events.append(("c", x, y, str(button)))

    # Create the listener objects
    keyboard_listener = KeyboardListener(on_press=on_press)
    mouse_listener = MouseListener(on_move=on_move, on_click=on_click)

    # Start the listeners
    keyboard_listener.start()
    mouse_listener.start()
    print("Started listening")