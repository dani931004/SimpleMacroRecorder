#!/usr/bin/python3
import pyautogui as pa
from time import sleep, time
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
# from recorder import play_recorder
from pynput.keyboard import Key, Listener
from recorder import play_recorder
from multiprocessing import Process

# Play recorded positions

# --- classes ---

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
       
        
switch,super,minutes,hours,seconds = False,0,0,0,0
class App():

    def __init__(self):
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
            global switch
            if key == Key.f12:
                # Stop listener
                switch = True
                return False            
               
        def clock_record():
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
            # open the mouse log file and take all x,y and buttons from it
            with open('mouse_log.txt', 'r') as f:
                # file = f.readlines()
                # a = tuple(file)
                for line in f:
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
                        elif 'ctrl' in line0:
                            press = "ctrlleft"
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
