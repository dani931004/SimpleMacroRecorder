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
#        3h    5m 5sec
super = 10800+300+59  # 11105
minutes = int(super/60)
hours = int(minutes/60)
if minutes >= 60:
    minutes = minutes-60*hours
if super >= 60:
    super = int(((super/3600)-hours)*60)
    print(super)

sleep(0.001)
print('Recorded for : {}:{}:{} time'.format(int(hours),int(minutes),int(super)))