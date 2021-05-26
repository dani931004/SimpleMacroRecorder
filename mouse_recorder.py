
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput import keyboard
import sys
import logging

# format='%(asctime)s: %(message)s' --> to see when the key is pressed or clicked or scrolled
logging.basicConfig(filename="mouse_log.txt", filemode='w', level=logging.DEBUG, format='%(message)s')

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('{0},{1},{2}'.format(x,y,button))

def on_scroll(x, y, dx, dy):
    logging.info('{0},{1},scrollh{2},{3}'.format(x, y, dx, dy))

mouse_listener = MouseListener(on_click=on_click, on_scroll=on_scroll)
mouse_listener.start()

def on_release(key):
    if key == keyboard.Key.f12:
        # Stop listener
        mouse_listener.stop()
        return sys.exit()
    else:
        logging.info('KeyUp:"{0}"'.format(key))
    
    
def on_press(key):
    if key == keyboard.Key.f12:
        # Stop listener
        mouse_listener.stop()
        return sys.exit()
    else:
        logging.info('Press:"{0}" '.format(key))
    


def play_recorder():
    # Setup the listener threads
    keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

    # Start the threads and join them so the script doesn't end early
    keyboard_listener.start()
    keyboard_listener.join()
    

