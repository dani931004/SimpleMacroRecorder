from time import time, sleep
from pynput import keyboard
from pynput.mouse import Controller
from pynput.mouse import Button
from pynput.keyboard import Key
from pynput import keyboard
import readline

keyDictionary = {
    "Key.alt":Key.alt,
    "Key.alt_l":Key.alt_l,
    "Key.alt_r":Key.alt_r,
    "Key.alt_gr":Key.alt_gr,
    "Key.backspace":Key.backspace,
    "Key.caps_lock":Key.caps_lock,
    "Key.cmd":Key.cmd,
    "Key.cmd_l":Key.cmd_l,
    "Key.cmd_r":Key.cmd_r,
    "Key.ctrl":Key.ctrl,
    "Key.ctrl_l":Key.ctrl_l,
    "Key.ctrl_r":Key.ctrl_r,
    "Key.delete":Key.delete,
    "Key.down":Key.down,
    "Key.end":Key.end,
    "Key.enter":Key.enter,
    "Key.esc":Key.esc,
    "Key.f1":Key.f1,
    "Key.f2":Key.f2,
    "Key.f3":Key.f3,
    "Key.f4":Key.f4,
    "Key.f5":Key.f5,
    "Key.f6":Key.f6,
    "Key.f7":Key.f7,
    "Key.f8":Key.f8,
    "Key.f9":Key.f9,
    "Key.f10":Key.f10,
    "Key.f11":Key.f11,
    "Key.f12":Key.f12,
    "Key.f13":Key.f13,
    "Key.f14":Key.f14,
    "Key.f15":Key.f15,
    "Key.f16":Key.f16,
    "Key.f17":Key.f17,
    "Key.f18":Key.f18,
    "Key.f19":Key.f19,
    "Key.f20":Key.f20,
    "Key.home":Key.home,
    "Key.left":Key.left,
    "Key.page_down":Key.page_down,
    "Key.page_up":Key.page_up,
    "Key.right":Key.right,
    "Key.shift":Key.shift,
    "Key.shift_l":Key.shift_l,
    "Key.shift_r":Key.shift_r,
    "Key.space":Key.space,
    "Key.tab":Key.tab,
    "Key.up":Key.up,
    "Key.media_play_pause":Key.media_play_pause,
    "Key.media_volume_mute":Key.media_volume_mute,
    "Key.media_volume_down":Key.media_volume_down,
    "Key.media_volume_up":Key.media_volume_up,
    "Key.media_previous":Key.media_previous,
    "Key.media_next":Key.media_next,
    "Key.insert":Key.insert,
    "Key.menu":Key.menu,
    "Key.num_lock":Key.num_lock,
    "Key.pause":Key.pause,
    "Key.print_screen":Key.print_screen,
    "Key.scroll_lock":Key.scroll_lock}

keyring = keyDictionary.keys()
valuering = keyDictionary.values()
mouse = Controller()
key_board = keyboard.Controller()

def play():
    go = time()
    '''Open the mouse log file 
        and take all x,y and buttons from it'''
    with open('mouse_log.txt', 'r') as f:
        for line in f:
            mouse_position = mouse.position
            if mouse_position == (0, 0):
                break
            '''Check if button or mouse press
                is present for every line,
                and then perform it'''
            if 'click' in line:
                line_part = line.split(',')
                sleep(float(line_part[4]))
                # mouse.position = (int(line_part[1]), int(line_part[2]))

                if 'left' in line_part[3]:
                    mouse.press(Button.left)

                elif 'right' in line_part[3]:
                    mouse.press(Button.right)

                else:
                    mouse.press(Button.middle)

            elif 'release' in line:
                line_part = line.split(',')
                sleep(float(line_part[4]))
                # mouse.position = (int(line_part[1]), int(line_part[2]))

                if 'left' in line_part[3]:
                    mouse.click(Button.left, 1)
                    mouse.release(Button.left)

                elif 'right' in line_part[3]:
                    mouse.click(Button.right, 1)
                    mouse.release(Button.right)

                else:
                    mouse.click(Button.middle, 1)
                    mouse.release(Button.middle)
            
            elif 'scroll' in line:
                line_part = line.split(',')
                sleep(float(line_part[5]))
                mouse.position = (int(line_part[1]), int(line_part[2]))
                mouse.scroll(int(line_part[3]), int(line_part[4]))

            elif 'move'in line:
                line_part = line.split(',')
                sleep(float(line_part[3]))
                mouse.position = (int(line_part[1]), int(line_part[2]))
            
            elif 'press' in line:
                line_part = line.split(',')                            
                
                if "press,','" in line:
                    key = ','
                    sleep(float(line_part[3]))
                elif '\\' in line:
                    sleep(float(line_part[2]))
                    key = '\\'.replace('\'','')
                elif 'press,"' in line:
                    sleep(float(line_part[2]))
                    key = "'"
                else:
                    sleep(float(line_part[2]))
                    key = ('{}'.format(line_part[1].replace("'","")))
                if key in keyring:
                    if key == "Key.ctrl":
                        key_board.press(keyDictionary[key])
                    else:
                        key_board.press(keyDictionary[key])
                        key_board.release(keyDictionary[key])
                        key_board.release(Key.ctrl)
                        
                else:
                    key_board.press(key)
                    key_board.release(key)

    ready = time() - go
    return print('\nProgram completed for', ready,'sec')

