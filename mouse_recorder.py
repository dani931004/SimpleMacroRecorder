
from pynput.mouse import Listener
import logging
# format='%(asctime)s: %(message)s'
logging.basicConfig(filename="mouse_log.txt", filemode='w', level=logging.DEBUG, format='%(message)s')

# def on_move(x, y):
#     logging.info("{0}|{1}".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('{0},{1},{2}'.format(x,y,button))

def on_scroll(x, y, dx, dy):
    logging.info('{0},{1},scrollh{2},{3}'.format(x, y, dx, dy))

def play_recorder():
    # on_move=on_move, on_click=on_click, on_scroll=on_scroll
    with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

