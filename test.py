# import pyautogui as pa
# from time import sleep
# from pynput import keyboard
# import logging
# logging.basicConfig(filename="symbols2.txt", filemode='w', level=logging.DEBUG, format='%(message)s')

with open('mouse_log.txt','r') as f:
    a =f.readlines()
    for line in a:
        line = line.replace('Press:','').replace("'","").replace('\n','')
        print(line)