
from pynput.mouse import Listener as mouse_listener
from pynput.keyboard import Listener as key_listener
from pynput import keyboard
import sys
import logging
import time

start = time.time()


def play_recorder():
    global start
    # format='%(asctime)s: %(message)s'
    # --> to see when the key is pressed or clicked or scrolled
    logging.basicConfig(filename="mouse_log.txt",
                        filemode='w',
                        level=logging.DEBUG,
                        format='%(message)s')
    def on_click(x, y, button, pressed):
        global start
        if pressed:
            stopp = time.time() - start
            logging.info('{0},{1},{2},{3}'.format(x, y, button, stopp))
            start = time.time()


    def on_scroll(x, y, dx, dy):
        global start
        stopp = time.time() - start
        logging.info('{0},{1},scrollh{2},{3},{4}'.format(x, y, dx, dy, stopp))
        start = time.time()

    def on_release(key):
        if key == keyboard.Key.f12:
            # Stopp listener
            mouse_listener.stop()
            return sys.exit()


    def on_press(key):
        global start
        if key == keyboard.Key.f12:
            # Stopp listener
            mouse_listener.stop()
            return sys.exit()
        else:
            print(key)
            stopp = time.time() - start
            logging.info('Press:{0},{1}'.format(key, stopp))
            start = time.time()

    mouse_listen = mouse_listener(on_click=on_click, on_scroll=on_scroll)
    
    # Setup the listener threads
    keyboard_listen = key_listener(on_press=on_press, on_release=on_release)

    # Start the threads and join them so the script doesn't end early
    keyboard_listen.start()
    mouse_listen.start()
    # keyboard_listen.join()
    # mouse_listen.join()

    



        
        
