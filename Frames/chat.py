# ----- Imports -----

import tkinter as tk
from tkinter import ttk
import requests
import os
from Frames.scrollable_window import MessageWindow

# for testing if server is down
messages=[{"message": "Hello, WORLD!", "date": 163829424}]
message_labels = [] 


# ----- Chat Frame Class -----

class Chat(ttk.Frame):
    def __init__(self, container, background, **kwargs):
        super().__init__(container, **kwargs) #NOTE: canvans (=self) does not have a style becasue it is a tk-object, not a ttk-object

    # ----- Form -----

        # set columns weight
        self.columnconfigure(0, weight=1)

        # set row weight
        self.rowconfigure(0, weight=1)

    # ----- Content -----

        # ----- Frames -----

        # initiate frames
        self.message_window = MessageWindow(self, background=background) #class creates a Canvas harboring a "scrollable" Frame-object
        input_frame =ttk.Frame(self, padding=10)

        self.message_input = tk.Text(input_frame, height=4) #height in rows of text
        self.message_input.pack(expand=True, fill="both", side="left", padx=(0,10))

        # place frames
        self.message_window .grid(row=0, column=0, sticky="NSEW", pady=10)
        input_frame.grid(row=1, column=0, sticky="EW")

        # ----- Buttons -----

        # initiate buttons
        fetch_message = ttk.Button(input_frame, text="Fetch", command=self.get_messages, style="FetchButton.TButton")
        submit_message = ttk.Button(input_frame, text="Send", command=self.post_message, style="SendButton.TButton")

        # place buttons
        fetch_message.pack() #NOTE: .pack() and .grid() can be used together in the same application but not within the same frame
                             #NOTE: use .pack() for all other objects within input_frame
        submit_message.pack()
        # # uncomment for troubleshooting
        # print(self.winfo_children()) 
         
    # ----- Methods -----

    # method to get messages from server 
    def get_messages(self):
        # create global variable to allow other methods to access this variable
        global messages
        # get messages from API and convert reply to JSON
        messages = requests.get("http://167.99.63.70/messages").json()
        self.message_window.message_update_widget(messages, message_labels)
        self.after(150, lambda: self.message_window.yview_moveto(1.0)) #after 150ms scroll all the way to the bottom

    # method to post messages
    def post_message(self):
        text = self.message_input.get("1.0","end").strip()
        requests.post("http://167.99.63.70/messages", json={"message": text})
        self.message_input.delete("1.0", "end") #deletes text field content after sending
        self.get_messages() 