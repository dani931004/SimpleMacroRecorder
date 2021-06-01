import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
# import pyautogui as pa

# --- classes ---

class PopupWindow():
    def __init__(self, root):
        #self.root = root
        window = tk.Toplevel(root)
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
        button_open_log = tk.Button(self.root, text="Open log file", command=self.popup_window)
        button_open_log.pack(fill='x')

        button_showinfo = tk.Button(self.root, text="Record", command=self.popup_showinfo)
        button_showinfo.pack(fill='x')

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
