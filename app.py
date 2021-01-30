# ----- import libraries and modules -----
import tkinter as tk
import os
from Frames.chat import Chat

# ----- main window class -----
class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # ----- form -----

        # set size
        self.geometry("1200x500")

        # set column weight
        self.columnconfigure(0, weight=1)

        # set row weight
        self.rowconfigure(0, weight=1)

    # ----- aestetics -----

        # set custom taskbar icon
        self.iconphoto(False, tk.PhotoImage(file=f'Media{os.sep}chat_icon.png')) 

        # set title
        self.title("Chat App")

    # ----- Frames -----

        # initiate chat frame
        self.chat_frame =  Chat(self)

        # place chat_frame
        self.chat_frame.grid(row=0, column=0, sticky="NSEW")

root = Messenger()
root.mainloop()