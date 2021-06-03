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


# File: readline-example-3.py

file = open("mouse_log.txt")
go = time.time()
while 1:

    file.readlines(10000)

    if not file:

        break

    for line in file:
            if 'Button' in line:
                splitted_line = line.split(',')
                speed = splitted_line[3]
                sleep(float(speed))
                dx = splitted_line[0]
                dy = splitted_line[1]
                b = splitted_line[2].replace('Button.', '').replace('\n', '')
                buttons = b
                pa.click(x=int(dx), y=int(dy), button=buttons)
            elif 'scrollh' in line:
                lsplitted_line = line.split(',')
                speed = lsplitted_line[4]
                sleep(float(speed))
                s = lsplitted_line[3].replace('\n', '')
                sx = lsplitted_line[0]
                sy = lsplitted_line[1]
                pa.scroll(s, x=int(sx), y=int(sy))
            elif 'Press' in line:
                if "Press:','," in line:
                    line = line.split("'")
                    speed = line[2].replace(',', '').replace('\n', '')
                    sleep(float(speed))
                    line[0] = "Press:','"
                else:
                    line = line.split(',')
                    speed = line[1].replace('\n', '')
                    sleep(float(speed))
                line0 = line[0].replace('Press:', '').replace("'", "").replace('\n', '')
                if "shift_r" in line0:
                    press = 'shiftright'
                    pa.press(press)
                elif '""' in line0:
                    press = '"'
                    pa.press(press)
                elif 'ctrl_r' in line0:
                    press = "ctrlright"
                    pa.press(press)
                elif 'alt_r' in line0:
                    press = "altright"
                    pa.press(press)
                elif 'cmd' in line0:
                    press = "winleft"
                    pa.press(press)
                else:
                    press = line0.replace('"', "").replace(' ', '')
                    press = press.replace('Key.', '').replace('_', '')
                    pa.press(press)
file.close()
ready = time.time() - go
print('Ready for', ready,'sec')
