import pyautogui as pa
from time import sleep
import tkinter as tk
from tkinter import filedialog as fd


# Record number of positions where mouse is clicked or scrolled
def record():
    print('Starting after 3 sec...')
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Recording...')
    from recorder import play_recorder
    # Record mouse clicks and scrolls
    play_recorder()
    print('Record stopped...')
    print('Recording done...')
    return 'Finished!'


# Play recorded positions
def play():
    print('Waiting 3 sec...')
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Playing...')
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
                line = line.split(',')
                speed = line[1]
                sleep(float(speed))
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
                    print('ELSE')
                    print('Press', press)
    return 'Complete!'


# --- classes ---

class PopupWindow():
    def __init__(self, root):
        #self.root = root
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

class App():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Simple Macro Recorder')
        self.root.geometry('300x140+530+313')
        
        label = tk.Label(self.root, text='To stop recording press(F12)...').pack(side='top')
        
        button_open_log = tk.Button(self.root, text="Open log file", command=self.popup_window)
        button_open_log.pack(fill='x')

        button_record = tk.Button(self.root, text="Record", command=record)
        button_record.pack(fill='x')
        
        button_play = tk.Button(self.root, text="Play", command=play)
        button_play.pack(fill='x')

        button_close = tk.Button(self.root, text="Close", command=self.root.destroy)
        button_close.pack(fill='x')

    def run(self):
        self.root.mainloop()

    def popup_window(self):
        PopupWindow(self.root)

    def popup_showinfo(self):
        showinfo("ShowInfo", "Hello World!")
    
   
    

# --- main ---

app = App()
app.run()

