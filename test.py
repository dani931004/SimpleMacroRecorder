from time import sleep
import pyautogui as pa

# from pynput import keyboard
# import logging
# logging.basicConfig(filename="symbols2.txt",
# filemode='w',
# level=logging.DEBUG,
# format='%(message)s')

with open('mouse_log.txt', 'r') as f:
    a = f.readlines()
    for line in a:
        if 'Button' in line:
            splitted_line = line.split(',')
            speed = splitted_line[3]
            sleep(float(speed))
            dx = splitted_line[0]
            dy = splitted_line[1]
            b = splitted_line[2].replace('Button.', '').replace('\n', '')
            buttons = b
            pa.click(x=int(dx), y=int(dy), button=buttons)
            print('Click')
        elif 'scrollh' in line:
            lsplitted_line = line.split(',')
            speed = lsplitted_line[4]
            sleep(float(speed))
            s = lsplitted_line[3].replace('\n', '')
            sx = lsplitted_line[0]
            sy = lsplitted_line[1]
            pa.scroll(s, x=int(sx), y=int(sy))
            print('Scroll')
        elif 'Press' in line:
            line = line.split(',')
            speed = line[1]
            sleep(float(speed))
            ok = line[0].replace('Press:', '')
            line0 = ok.replace("'", "").replace('\n', '')
            if "shift_r" in line0:
                press = 'shiftright'
                pa.press(press)
                print('IF')
                print('Press', press)
            elif '""' in line0:
                press = '"'
                print('ELIF')
                pa.press(press)
                print('Press', press)
            elif 'ctrl_r' in line0:
                press = "ctrlright"
                pa.press(press)
                print('ELIF')
                print('Press', press)
            elif 'alt_r' in line0:
                press = "altright"
                pa.press(press)
                print('ELIF')
                print('Press', press)
            elif 'cmd' in line0:
                press = "winleft"
                pa.press(press)
                print('ELIF')
                print('Press', press)
            else:
                press = line0.replace('"', "").replace(' ', '')
                press = press.replace('Key.', '').replace('_', '')
                pa.press(press)
                print('ELSE')
                print('Press', press)
