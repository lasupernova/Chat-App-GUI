# ----- import libraries and modules -----
import tkinter as tk
from tkinter import ttk
import os
import tkinter.font as font
from Frames.chat import Chat

# ----- Custom Variables -----

# COLORS
COLOUR_LIGHT_BACKGROUND_1 = "#fff"
COLOUR_LIGHT_BACKGROUND_2 = "#f2f3f5"
COLOUR_LIGHT_BACKGROUND_3 = "#e3e5e8"
COLOUR_LIGHT_TEXT = "#aaa"
COLOUR_DARK_TEXT = "#c1b6c2"
COLOUR_BUTTON_NORMAL = "#5fba7d"
COLOUR_BUTTON_ACTIVE = "#58c77c"
COLOUR_BUTTON_PRESSED = "#44e378"


# ----- main window class -----
class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # ----- form -----

        # set size
        self.geometry("1200x500")

        # set minimum size
        self.minsize(400, 300)

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
        self.chat_frame =  Chat(self, background=COLOUR_LIGHT_BACKGROUND_1, style="Messages.TFrame")

        # place chat_frame
        self.chat_frame.grid(row=0, column=0, sticky="NSEW")

# start app
root = Messenger()

# ----- Styles -----
font.nametofont("TkDefaultFont").configure(size=14)

style = ttk.Style(root)
style.theme_use("clam")

style.configure(
    "Messages.TFrame", 
    background=COLOUR_LIGHT_BACKGROUND_3)

style.configure(
    "Controls.TFrame", 
    background=COLOUR_LIGHT_BACKGROUND_2)

style.configure(
    "SendButton.TButton", 
    borderwidth=0, 
    background=COLOUR_BUTTON_NORMAL)
style.map(
    "SendButton.TButton",
    background=[("pressed", COLOUR_BUTTON_PRESSED), ("active", COLOUR_BUTTON_ACTIVE)],
)

style.configure(
    "FetchButton.TButton", 
    background=COLOUR_LIGHT_BACKGROUND_1, 
    borderwidth=0
)

style.configure(
    "Time.TLabel",
    padding=5,
    foreground=COLOUR_DARK_TEXT,
    font=8
)

style.configure(
    "Avatar.TLabel", 
    background=COLOUR_LIGHT_BACKGROUND_3)

style.configure(
    "Message.TLabel", 
    background=COLOUR_LIGHT_BACKGROUND_2)

# run loop
root.mainloop()