'''
Class creating a scrollable window within a ttk.Canvas-Object
'''

# -----Imports -----
import tkinter as tk
from tkinter import ttk
import datetime
from PIL import Image, ImageTk
import os

# ----- class creating scrollable Canvas window -----
class MessageWindow(tk.Canvas):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs, highlightthickness=0)

    # ----- Frames -----

        # create new Frame object in Canvas and configure
        self.message_frame = ttk.Frame(self)
        self.message_frame.columnconfigure(0, weight=1)

        # make self.message_frame a window within the Canvas (=self) and configure
        self.scrollable_window = self.create_window((0, 0), window=self.message_frame, anchor="nw")

        #  function configuring Canvas scrolling abilities
        def configure_scroll_region(event):
            # set (the size of the) scrollable area to entail all objects within the canvas
            self.configure(scrollregion=self.bbox("all"))

        # function to limit scrolling to y-axis
        def configure_window_size(event):
            # set Canvas size (width) to scrollable_window width
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        # trigger scrolling depending on what is done in window (e.g. moving scrollbar or turning mousewheel)
        self.bind("<Configure>", configure_window_size)
        self.message_frame.bind("<Configure>", configure_scroll_region) 
        self.bind_all("<MouseWheel>", self._on_mousewheel) #use .bind_all() because function should be triggered, no matter what widget/object is currently selected

        # create Scrollbar object and place
        scrollbar = ttk.Scrollbar(container, orient="vertical",command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        # trigger condigure command whenever the scrollbar is used
        self.configure(yscrollcommand=scrollbar.set)

        # define how sensitive scrolling should be
        self.yview_moveto(1.0)


    # ------ Methods -----

    # internal method, activating scrolling when mouse wheel is turned
    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta/120), "units")

       # method, printing new messages to message_frame
    def message_update_widget(self, messages, message_labels):

        # save already displayed message texts and dates in list, NOTE: message_labels stores ttk.Label-objects (one for message-text and one for the message-datetime per message) - the text stored within these objects is stored in the list
        displayed_messages = [(message["text"], time["text"]) for message, time in message_labels]

        # iterate over new messages
        for message in messages:

            # extract message time and convert into readable string
            message_time = datetime.datetime.fromtimestamp(message["date"]).strftime("%d-%m-%Y %H:%M:%S")

            # check that message was not previously displayed 
            if (message["message"], message_time )not in displayed_messages:
                self._create_message_container(message["message"], message_time, message_labels) 

        print("All messages displayed!")


    # private method creating message container 
    def _create_message_container(self, message_content, message_time, message_labels):

        # create a container to display current message and date in 
        container = ttk.Frame(self.message_frame)

        # configure second column to expand and take up available space
        container.columnconfigure(1, weight=1)

        # place container
        container.grid(sticky="EW", padx=(10,50),pady=10)

        # call method to create/insert actual content to be displayed into container
        self._create_message_bubble(container, message_content, message_time, message_labels)


    # -----private method inserting content to be displayed to container-----
    def _create_message_bubble(self, container, message_content, message_time, message_labels):

        # create message-avatar
        dirname = os.path.dirname(__file__) #current dir
        filename = os.path.join(dirname, f'..{os.sep}Media{os.sep}user_icon.png') #path to .png image
        user_image = Image.open(filename) #open image
        user_image = user_image.resize((30,30),Image.ANTIALIAS) #resize image
        user_photo = ImageTk.PhotoImage(user_image) #make image Tkinter compatible

        # create Label to display user image
        image_label = ttk.Label(
            container,
            image=user_photo
        )
        image_label.image = user_photo #persist image.label --> without this step, the image will be deleted from image_label and will not be shown
        image_label.grid(row=0, column=0, rowspan=2, sticky="NEW", padx=(0,10), pady=(5,0))

        # create new lable per new message
        time_label = ttk.Label(
                        container,
                        text=message_time
                        )

        # add current label to message_frame
        time_label.grid(row=0, column=1, sticky="NEW")


        # create new label per new message
        message_label = ttk.Label(
                        container,
                        text=message_content, #get text from current message
                        anchor="w",
                        justify="left",
                        wraplength="1000" #wrap text at 900 pixels of text-width
                        )

        # add current label to message_frame
        message_label.grid(row=1, column=1, sticky="NSEW")

        # add message to displayed messages
        message_labels.append((message_label, time_label))


