from tkinter import *
from tkinter import messagebox
from Api.api import make_general_channel_request, make_channel_video_titles_and_dates_request
channel_id = ""

def channel_component(window):
    global channel_id_entry, get_title_and_dates_button
    enter_channel_id_label = Label(window, bg='bisque', text="Enter channel ID: ")
    enter_channel_id_label.grid(column=0, row=1, padx=2, pady=2)
    
    channel_id_entry = Entry(window, width=40)
    channel_id_entry.grid(column=1, row=1)
    
    get_channel_id_button = Button(window, width=20, text="GO", fg="Blue4", bg="SkyBlue3", 
                                                                    command=get_channel_id)
    get_channel_id_button.grid(column=2, row=1, padx=2, pady=2)
    
    get_title_and_dates_button = Button(window, width=20, text="Videos and publishing dates", fg="Blue4", bg="SkyBlue3", 
                                                                    command=get_titles_and_dates, state=DISABLED)
    get_title_and_dates_button.grid(column=4, row=1, padx=2, pady=2)
    
def get_channel_id():
    global channel_id
    channel_id = channel_id_entry.get()
    response = make_general_channel_request(channel_id)
    if response != "error":
        get_title_and_dates_button.configure(state=NORMAL)
    else:
    #messagebox.showinfo('COPIED!', f"The video ID: {video_id} has been copied to your clipboard!")
        get_title_and_dates_button.configure(state=DISABLED)  # Disable the button
        return channel_id

def get_titles_and_dates():
    global channel_id
    titles_and_dates = make_channel_video_titles_and_dates_request(channel_id)
    messagebox.showinfo('TITLES AND PUBLISHING DATES', f"{titles_and_dates}")
    return titles_and_dates
