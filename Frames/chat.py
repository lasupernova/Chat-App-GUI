# ----- Imports -----

from tkinter import ttk
import requests
import os
from Frames.scrollable_window import MessageWindow

# for testing if server is down
messages=[{"message": "Hello, WORLD!", "date": 163829424}]
message_labels = [] 


# ----- Chat Frame Class -----

class Chat(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

    # ----- Form -----

        # set columns weight
        self.columnconfigure(0, weight=1)

        # set row weight
        self.rowconfigure(0, weight=1)

    # ----- Content -----

        # ----- Frames -----

        # initiate frames
        self.message_window = MessageWindow(self) #class creates a Canvas harboring a "scrollable" Frame-object
        input_frame =ttk.Frame(self, padding=10)

        # place frames
        self.message_window .grid(row=0, column=0, sticky="NSEW", pady=10)
        input_frame.grid(row=1, column=0, sticky="EW")

        # ----- Buttons -----

        # initiate buttons
        fetch_message = ttk.Button(input_frame, text="Fetch", command=self.get_messages)

        # place buttons
        fetch_message.pack() #NOTE: .pack() and .grid() can be used together in the same application but not within the same frame
                             #NOTE: use .pack() for all other objects within input_frame

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