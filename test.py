import pyautogui as pa
from time import sleep
from pynput import keyboard
import logging
# logging.basicConfig(filename="symbols2.txt", filemode='w', level=logging.DEBUG, format='%(message)s')
speed = input('Please enter the speed between clicks in sec...')
print('Waiting 3 sec...')
print('3...')
sleep(1)
print('2...')
sleep(1)
print('1...')
sleep(1)
print('Playing...')
with open('symbols2.txt', 'r') as f:
    a = f.readlines()
    for symbol in a:
        symbol = symbol.replace('\n','')
        pa.press(symbol)
        print(symbol)
        sleep(float(speed))