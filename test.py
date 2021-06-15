from time import time, sleep
from pynput.keyboard import Controller as key_ctrl
from pynput.mouse import Controller
from pynput.mouse import Button

mouse = Controller()
keyboard = key_ctrl


def play():
            go = time()
            '''open the mouse log file 
               and take all x,y and buttons from it'''
            with open('mouse_log.txt', 'r') as f:
                for line in f:
                    if 'click' in line:
                        line_part = line.split(',')
                        sleep(float(line_part[4]))
                        mouse.position = (int(line_part[1]),int(line_part[2]))
                        if 'left' in line_part[3]:
                            mouse.click(Button.left,1)
                        else:
                            mouse.click(Button.right,1)
                    # elif 'scrollh' in line:
                    #     lline_part = line.split(',')
                    #     speed = lline_part[4]
                    #     sleep(float(speed))
                    #     s = lline_part[3].replace('Button.','').replace('\n', '')
                    #     sx = lline_part[0]
                    #     sy = lline_part[1]
                    #     pa.scroll(s, x=int(sx), y=int(sy))
                    # elif 'Press' in line:
                    #     if "Press:','," in line:
                    #         line = line.split("'")
                    #         speed = line[2].replace(',', '').replace('\n', '')
                    #         sleep(float(speed))
                    #         line[0] = "Press:','"
                    #     else:
                    #         line = line.split(',')
                    #         speed = line[1].replace('\n', '')
                    #         sleep(float(speed))
                    #     line0 = line[0].replace('Press:', '').replace("'", "").replace('\n', '')
                    #     if "shift_r" in line0:
                    #         press = 'shiftright'
                    #         pa.press(press)
                    #     elif '""' in line0:
                    #         press = '"'
                    #         pa.press(press)
                    #     elif 'ctrl' in line0:
                    #         press = "ctrlleft"
                    #         pa.press(press)
                    #     elif 'alt_r' in line0:
                    #         press = "altright"
                    #         pa.press(press)
                    #     elif 'cmd' in line0:
                    #         press = "winleft"
                    #         pa.press(press)
                    #     else:
                    #         press = line0.replace('"', "").replace(' ', '')
                    #         press = press.replace('Key.', '').replace('_', '')
                    #         pa.press(press)
            ready = time() - go
            return print('Ready for', ready,'sec')

play()