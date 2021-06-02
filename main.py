#!/usr/bin/python3
import pyautogui as pa
from time import sleep
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from recorder import play_recorder
from pynput.keyboard import Key, Listener

# Play recorded positions
def play():
    # open the mouse log file and take all x,y and buttons from it
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
                if "Press:','," in line:
                    line = line.split("'")
                    speed = line[2].replace(',', '').replace('\n', '')
                    sleep(float(speed))
                    line[0] = "Press:','"
                    print('if')
                else:
                    line = line.split(',')
                    speed = line[1].replace('\n', '')
                    sleep(float(speed))
                    print('else')
                line0 = line[0].replace('Press:', '').replace("'", "").replace('\n', '')
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
                    print('Final ELSE')
                    print('Press', press)
    return 'Complete!'


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
       
        
Recorderr = True
super = 0
class App():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Simple Macro Recorder')
        self.root.geometry('300x185+530+313')

        label = tk.Label(self.root, text='To stop recording press(F12)...')
        label.pack(side='top')
        label2 = tk.Label(self.root, text='''Upper left corner with mouse to stop Play...''')
        label2.pack(side='top')

        button_open_log = tk.Button(self.root, text="Open log file", command=self.popup_window)
        button_open_log.pack(fill='x')
        def record():
            clock()
            play_recorder()
            # Collect all event until released
            listener = Listener(on_press = show)
            listener.start()
        def show(key):
            print('\nYou Entered {0}'.format( key))
            if key == Key.f12:
                # Stop listener
                button_record.config(text='STOP', command=record)
                return False
        
        
            
            
        def clock():
            
            global super
            super = super + 1
            button_record.config(text='Elapsed time: '+str(int(super))+' sec',command=self.popup_info)
            button_record.after(1000, clock)

        button_record = tk.Button(self.root, text="Record", command=record)
        button_record.pack(fill='x')
        
        button_play = tk.Button(self.root, text="Play", command=play)
        button_play.pack(fill='x')

        button_close = tk.Button(self.root, text="Close", command=self.root.destroy)
        button_close.pack(fill='x')

    def run(self):
        self.root.mainloop()

    def popup_window(self):
        PopupWindow1(self.root)
   
    def popup_info(self):
        showinfo("Recording...", "Recording, please press(F12) to stop!")

        
        


# --- main ---
app = App()
app.run()
