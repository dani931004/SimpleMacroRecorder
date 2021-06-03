#!/usr/bin/python3
import pyautogui as pa
from time import sleep
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
# from recorder import play_recorder
from pynput.keyboard import Key, Listener
from recorder import play_recorder
import time

# start = time.time()
# sleep(2)
# stop = time.time() - start
# stop = int(stop)
# print(stop)

seconds = 0
minutes = 0
hours = 0
while hours < 2:
    seconds += 1
    if seconds >= 60:
        seconds = 0
        minutes += 1
        if minutes >=60:
            seconds = 0
            minutes = 0
            hours += 1
    sleep(0.1)
    print('Recorded for : {}:{}:{} time'.format(hours,minutes,seconds))