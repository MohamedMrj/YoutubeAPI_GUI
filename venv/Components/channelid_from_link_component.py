from tkinter import *
from tkinter import messagebox
from Api.api import clean_channel_link
import pyperclip as pc


def youtube_channel_link(window):
    global youtube_channel_link_entry, copy_channel_id_button, show_channel_id_button
    enter_youtube_channel_link = Label(window, bg='bisque', text="Enter Youtube Channel Link: ")
    enter_youtube_channel_link.grid(column=0, row=0, padx=2, pady=2)
    
    youtube_channel_link_entry = Entry(window, width=40)
    youtube_channel_link_entry.grid(column=1, row=0)
    
    get_channel_id_from_link_button = Button(window, width=20, text="Get ID", fg="Blue4", bg="SkyBlue3", 
                                                                    command=get_channel_id_from_link)
    get_channel_id_from_link_button.grid(column=2, row=0, padx=2, pady=2)
    
    copy_channel_id_button = Button(window, width=20, text="COPY ID", fg="Blue4", bg="SkyBlue3", 
                                                                    command=copy_channel_id, state=DISABLED)
    copy_channel_id_button.grid(column=4, row=0, padx=2, pady=2)
    
    show_channel_id_button = Button(window, width=20, text="SHOW ID", fg="Blue4", bg="SkyBlue3", 
                                                                    command=show_channel_id, state=DISABLED)
    show_channel_id_button.grid(column=5, row=0, padx=2, pady=2)
def get_channel_id_from_link():
    global channel_id
    link_from_entry = youtube_channel_link_entry.get()
    print(link_from_entry)
    channel_id = clean_channel_link(link_from_entry)
    if channel_id != "error":
        copy_channel_id_button.configure(state=NORMAL)
        show_channel_id_button.configure(state=NORMAL)
        print(channel_id)
        return channel_id
    else:
    #messagebox.showinfo('COPIED!', f"The video ID: {video_id} has been copied to your clipboard!")
        copy_channel_id_button.configure(state=DISABLED)
        show_channel_id_button.configure(state=DISABLED)
        print(channel_id)
        return channel_id
    
def copy_channel_id():
    pc.copy(channel_id)
    paste = pc.paste()
    messagebox.showinfo("COPIED ID", paste)

def show_channel_id():
    messagebox.showinfo("Channel ID", f"This is the channel ID: {channel_id}")