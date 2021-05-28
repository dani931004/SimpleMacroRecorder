
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput import keyboard
import sys
import logging
import time
start = time.time()
# format='%(asctime)s: %(message)s' --> to see when the key is pressed or clicked or scrolled
logging.basicConfig(filename="mouse_log.txt", filemode='w', level=logging.DEBUG, format='%(message)s')
def on_click(x, y, button, pressed):
    global start
    if pressed:
        stop = time.time() - start
        logging.info('{0},{1},{2},{3}'.format(x,y,button,stop))
        start = time.time()

def on_scroll(x, y, dx, dy):
    global start
    stop = time.time() - start
    logging.info('{0},{1},scrollh{2},{3},{4}'.format(x, y, dx, dy,stop))
    start = time.time()

mouse_listener = MouseListener(on_click=on_click, on_scroll=on_scroll)
mouse_listener.start()



def on_release(key):
    if key == keyboard.Key.f12:
        # Stop listener
        mouse_listener.stop()
        return sys.exit()
    
    
def on_press(key):
    global start
    if key == keyboard.Key.f12:
        # Stop listener
        mouse_listener.stop()
        return sys.exit()
    else:
        print(key)
        logging.info('Press:{0}'.format(key))
        stop = time.time() - start

        start = time.time()
    


def play_recorder():
    global start
    # Setup the listener threads
    keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

    # Start the threads and join them so the script doesn't end early
    keyboard_listener.start()
    keyboard_listener.join()
    start = time.time()
    

