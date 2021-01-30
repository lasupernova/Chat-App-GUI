# ----- Imports -----

from tkinter import ttk
import requests
import datetime

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
        self.message_frame = ttk.Frame(self)
        input_frame =ttk.Frame(self, padding=10)

        # place frames
        self.message_frame.grid(row=0, column=0, sticky="NSEW", pady=10)
        input_frame.grid(row=1, column=0, sticky="EW")

        # ----- Buttons -----

        # initiate buttons
        fetch_message = ttk.Button(input_frame, text="Fetch", command=self.get_messages)

        # place buttons
        fetch_message.pack() #NOTE: .pack() and .grid() can be used together in the same application but not within the same frame
                             #NOTE: use .pack() for all other objects within input_frame
         
    # ----- Methods -----

    # method to get messages from server 
    def get_messages(self):
        # create global variable to allow other methods to access this variable
        global messages
        # get messages from API and convert reply to JSON
        messages = requests.get("http://167.99.63.70/messages").json()
        self.message_update_widget()

    # method printing new messages to message_frame
    def message_update_widget(self):

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

        # create new label per new message
        time_label = ttk.Label(
                        container,
                        text=message_time
                        )

        # add current label to message_frame
        time_label.grid(row=0, column=0, sticky="NEW")


        # create new label per new message
        message_label = ttk.Label(
                        container,
                        text=message_content, #get text from current message
                        anchor="w",
                        justify="left"
                        )

        # add current label to message_frame
        message_label.grid(row=1, column=0, sticky="NSEW")

        # add message to displayed messages
        message_labels.append((message_label, time_label))