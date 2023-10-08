from tkinter import *
from tkinter import messagebox
from Api.api import make_general_video_request, make_view_count_request, make_like_count_request, make_comment_count_request

# Define a global variable to store the video_id
video_id = ""

def video_component(window):
    
    global video_id_entry, get_views_count_button, get_likes_count_button, get_comments_count_button
    
    enter_video_id_label = Label(window,bg='bisque', text="Enter video ID: ")
    enter_video_id_label.grid(column=0, row=2, padx=2, pady=2)
    
    video_id_value = StringVar()
    
    video_id_entry = Entry(window, width=40, textvariable=video_id_value)
    video_id_entry.grid(column=1, row=2, padx=2, pady=2)
    
    get_video_id_button = Button(window, width=20, text="GO", fg="dark green", bg="SkyBlue3", 
                                                                    command=get_video_id)
    get_video_id_button.grid(column=2, row=2, padx=2, pady=2)

    get_views_count_button = Button(window, width=20, text="View Count", bg="SkyBlue3", 
                                                                    command=get_views_count, state=DISABLED)
    get_views_count_button.grid(column=0, row=3, padx=2, pady=2)

    get_likes_count_button = Button(window, width=20, text="Likes Count", bg="SkyBlue3", 
                                                                    command=get_likes_count, state=DISABLED)
    get_likes_count_button.grid(column=1, row=3, padx=2, pady=2)
    
    get_comments_count_button = Button(window, width=20, text="Comments Count", bg="SkyBlue3", 
                                                                    command=get_comments_count, state=DISABLED)
    get_comments_count_button.grid(column=2, row=3, padx=2, pady=2)


def get_video_id():
    global video_id, get_views_count_button  # Access the global button
    video_id = video_id_entry.get()
    response = make_general_video_request(video_id)
    if response != "error":
        get_views_count_button.configure(state=NORMAL)  # Enable the button
        get_likes_count_button.configure(state=NORMAL)
        get_comments_count_button.configure(state=NORMAL)
    else:
        #messagebox.showinfo('COPIED!', f"The video ID: {video_id} has been copied to your clipboard!")
        get_views_count_button.configure(state=DISABLED)  # Disable the button
        get_views_count_button.configure(state=DISABLED)
        get_comments_count_button.configure(state=DISABLED)

    return response
def get_views_count():
    global video_id
    view_count = make_view_count_request(video_id)
    messagebox.showinfo('VIEWS COUNT', f"View count is: {view_count} views")
    return view_count

def get_likes_count():
    global video_id
    likes_count = make_like_count_request(video_id)
    messagebox.showinfo("LIKES COUNT", f"Likes count is: {likes_count}!")
    return likes_count

def get_comments_count():
    global video_id
    comments_count = make_comment_count_request(video_id)
    messagebox.showinfo("COMMENTS COUNT", f"Comments count is: {comments_count}!")
    return comments_count