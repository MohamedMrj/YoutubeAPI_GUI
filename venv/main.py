from tkinter import *

from Components.channel_component import channel_component
from Components.video_component import *
from Components.channelid_from_link_component import youtube_channel_link

def main():
    window = Tk()
    youtube_channel_link(window)
    channel_component(window) #get Channel Component #
    video_component(window)
    
    info = Label(window, bg="LightGoldenrod4",
                text="This is a simple GUI made to get information about a specific youtube channel or video \n Made By Mohamed Almefrej ")
    info.grid(row=19, column=0, padx=3, pady=3, sticky="e")
    
    window.geometry("1200x200")
    window.configure(bg='midnight blue')
    window.mainloop()

if __name__ == "__main__":
    main()