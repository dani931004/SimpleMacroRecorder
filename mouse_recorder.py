
from pynput.mouse import Listener
import logging
# format='%(asctime)s: %(message)s'
logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(message)s')

def on_move(x, y):
    logging.info("{0}|{1}".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:

        logging.info('{0}'.format(button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

def play_listener(*kwargs):
    # on_move=on_move, on_click=on_click, on_scroll=on_scroll
    if 'on_click' in kwargs:
        with Listener(on_click=on_click) as listener:
            listener.join()
            return 'On_click'
    elif 'on_move' in kwargs:
        with Listener(on_move=on_move) as listener:
            listener.join()
            return 'On_move'
    elif 'on_scroll' in kwargs:
        with Listener(on_scroll=on_scroll) as listener:
            listener.join()
            return 'On_scroll'
    elif 'all' in kwargs:
        with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
            listener.join()
            return 'all'
    else:
        return "This mode doesn't exist"
