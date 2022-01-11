from pynput.mouse import Listener as mouse_listener
from pynput.keyboard import Listener as key_listener
from pynput import keyboard
import logging
import time
import readline

def play_recorder():
    global start
    logging.basicConfig(filename="mouse_log.txt",
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(message)s')
    
    start = time.time()
    # format='%(asctime)s: %(message)s'
    # --> to see when the key is pressed or clicked or scrolled

    def on_move(x, y):
        global start
        stopp = time.time() - start
        logging.info(f'move,{x},{y},{stopp}')
        # print(f'move,{x},{y}')
        start = time.time()
        
    def on_click(x, y, button, pressed):
        global start
        if pressed:
            stopp = time.time() - start
            logging.info('click,{0},{1},{2},{3}'.format(x, y, button, stopp))
            print('click,{0},{1},{2},{3}'.format(x, y, button, stopp))
            start = time.time()
        else:
            stopp = time.time() - start
            logging.info('release,{0},{1},{2},{3}'.format(x, y, button, stopp))
            print('release,{0},{1},{2},{3}'.format(x, y, button, stopp))
            start = time.time()


    def on_scroll(x, y, dx, dy):
        global start
        stopp = time.time() - start
        logging.info('scroll,{0},{1},{2},{3},{4}'.format(x, y, dx, dy, stopp))
        # print('scroll,{0},{1},{2},{3},{4}'.format(x, y, dx, dy, stopp))
        start = time.time()

    def on_press(key):
        global start
        if key == keyboard.Key.f12:
            # Stopp listener
            mouse_listen.stop()
            keyboard_listen.stop()
            print("\nRecorder has been stoped!\n")
            return False
        else:
            stopp = time.time() - start
            logging.info('press,{0},{1}'.format(key, stopp))
            # print('press,{0},{1}'.format(key, stopp))
            start = time.time()
    
    keyboard_listen = key_listener(on_press=on_press)
    keyboard_listen.start()
    
    with mouse_listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listen:
        mouse_listen.join()
    # Setup the listener threads
    
        #, on_release=on_release

    # Start the threads and join them so the script doesn't end early
    
    

