'''Make dragging mouse and
   keyboard keys possible'''

'''Next make moving mouse appear on record'''

#!/usr/bin/python3

import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from pynput.keyboard import Key, Listener
from test_recorder import play_recorder
from multiprocessing import Process
from time import time, sleep
from pynput import keyboard
from pynput.mouse import Controller
from pynput.mouse import Button
from pynput.keyboard import Key


class PopupWindow1():
    def __init__(self, root):
        # self.root = root
        window = tk.Toplevel(root)
        window.geometry('280x445+540+165')
        text = tk.Text(window)
        text.pack(side="top", fill="x")
        # file type
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        # show the open file dialog
        f = fd.askopenfile(filetypes=filetypes)
        # read the text file and show its content on the Text
        text.insert('1.0', f.readlines())

        button_close = tk.Button(window, text="Close", command=window.destroy)
        button_close.pack(fill='x')
       
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
switch,super,minutes,hours,seconds = False,0,0,0,0
class App():

    def __init__(self):
        '''Initiate the GUI window'''
        self.root = tk.Tk()
        self.root.title('Simple Macro Recorder')
        self.root.geometry('300x165+530+313')

        label = tk.Label(self.root, text='To stop recording press(F12)...')
        label.pack(side='top')
        label2 = tk.Label(self.root, text='''Upper left corner with mouse to stop Play...''')
        label2.pack(side='top')

        button_open_log = tk.Button(self.root, text="Open log file", command=self.popup_window)
        button_open_log.pack(fill='x')
        
        def record():
            '''Start recording'''
            global switch
            if switch == False:
                play_recorder()
                clock_record()
            else:
                switch = False
                clock_record()
                play_recorder()
            # Collect all event until released
            listener = Listener(on_press = show)
            listener.start()
        
        def show(key):
            '''Create switch to know when to 
               terminate recording'''
            global switch
            if key == Key.f12:
                # Stop listener
                switch = True
                return False            
               
        def clock_record():
            '''Make clock when recording is active
               and show how long was the recording'''
            global switch,super,minutes,hours,seconds
            if switch == False:
                super += 1
                seconds += 1
                if super % 60 == 0:
                    super = 0
                    minutes += 1
                if minutes >= 60:
                    minutes = 0
                    hours += 1
                button_record.config(text='Elapsed time: {}:{}:{} hours'.format(int(hours),int(minutes),int(super)),command=self.popup_info_record)
                button_record.after(1000, clock_record)
            else:
                minutes = int(seconds/60)
                hours = int(minutes/60)
                if minutes >= 60:
                    minutes = minutes-60*hours
                seconds = (seconds-(hours*3600))-(minutes*60)
                button_record.config(text='Recorded for {}:{}:{} hours'.format(int(hours),int(minutes),int(super)), command=record)
                seconds = 0
                super = 0
                hours = 0
                minutes = 0
                switch = False

        def play():
            go = time()
            '''Open the mouse log file 
               and take all x,y and buttons from it'''
            with open('mouse_log_test.txt', 'r') as f:
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
                        mouse.position = (int(line_part[1]), int(line_part[2]))

                        if 'left' in line_part[3]:
                            mouse.press(Button.left)

                        elif 'right' in line_part[3]:
                            mouse.press(Button.right)

                        else:
                            mouse.press(Button.middle)
                    
                    elif 'release' in line:
                        line_part = line.split(',')
                        sleep(float(line_part[4]))
                        mouse.position = (int(line_part[1]), int(line_part[2]))

                        if 'left' in line_part[3]:
                            mouse.release(Button.left)

                        elif 'right' in line_part[3]:
                            mouse.release(Button.right)

                        else:
                            mouse.release(Button.middle)

                    elif 'scroll' in line:
                        line_part = line.split(',')
                        sleep(float(line_part[5]))
                        mouse.position = (int(line_part[1]), int(line_part[2]))
                        mouse.scroll(int(line_part[3]), int(line_part[4]))

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
                            print('Pressing:',key)
                            key_board.press(keyDictionary[key])
                            key_board.release(keyDictionary[key])
                        else:
                            print('Pressing:',key)
                            key_board.press(key)
                            key_board.release(key)


            ready = time() - go
            return print('Ready for', ready,'sec')




        def play_process():
            process = Process(target=play)
            process.start()
            self.popup_info_play()
        

        button_record = tk.Button(self.root, text="Record", command=record)
        button_record.pack(fill='x')
        
        button_play = tk.Button(self.root, text="Play", command=play_process)
        button_play.pack(fill='x')

        button_close = tk.Button(self.root, text="Close", command=self.root.destroy)
        button_close.pack(fill='x')
        
    def run(self):
        self.root.mainloop()

    def popup_window(self):
        PopupWindow1(self.root)
   
    def popup_info_record(self):
        showinfo("Recording...", "Recording, please press(F12) to stop!")

    def popup_info_play(self):
        showinfo("Playing...","Go to upper left corner with mouse to interrupt!")
    
        
        


# --- main ---
app = App()
app.run()
