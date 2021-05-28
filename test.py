import pyautogui as pa
from time import sleep
# from pynput import keyboard
# import logging
# logging.basicConfig(filename="symbols2.txt", filemode='w', level=logging.DEBUG, format='%(message)s')
from datetime import datetime
from time import time

speed = 1
with open('mouse_log.txt', 'r') as f:
        a = f.readlines()
        case = '"'
        for line in a:
            
            if 'Button' in line:
                # l = line.split(',')
                # dx = l[0]
                # dy = l[1]
                # b = l[2].replace('Button.','').replace('\n','')
                # buttons = b
                # pa.click(x=int(dx), y=int(dy), button=buttons)
                sleep(float(speed))
                print('Click')