# API_Request.py
import json
import requests
from pytube import YouTube, Channel
import re


API_KEY = "PLACE YOUR API KEY HERE"

def clean_channel_link(link):
    global link_from_user
    link_from_user = str(link)
    if link_from_user.__contains__("@"):
        link_from_user = link_from_user.replace("@", "c/")
        channel_id = Channel(link_from_user).channel_id
        return channel_id
    else:
        channel_id = Channel(link_from_user).channel_id
        return channel_id



def make_general_channel_request(channel_id):
    """Make a request to get channel information."""
    URL = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}" + \
        f"&channelId={channel_id}" + \
        f"&part=snippet,id&order=date&maxResults=50"
    try:
        json_response = requests.get(URL).json()
        response = json.dumps(json_response, indent=2)
        return response
    except Exception as e:
        return f"Error: {e}"


def make_channel_video_titles_and_dates_request(channel_id):
    PAGETOKEN = ""
    URL = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}" + \
    f"&channelId={channel_id}" + \
    f"&part=snippet,id&order=date&maxResults=50&" + \
    f"pageToken={PAGETOKEN}"
    try:
        response = requests.get(URL).json()
        response_title_and_date = {}
        for snippet in response["items"]:
            title = snippet['snippet']['title']
            full_date = snippet["snippet"]["publishedAt"]
            if "T" in full_date:
                date = full_date[:10]  # YYYY-MM-DD
            response_title_and_date[title] = date #add title and date to title_and_date{} as pair(key:value)
        return response_title_and_date
    except Exception as e:
        return f"Error: {e}"


def make_general_video_request(video_id):
    """Make a request to get video information."""
    URL = f"https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails,"  + \
        f"statistics"  + \
        f"&id={video_id}&maxResults=50&" + \
        f"key={API_KEY}"
    try:
        response = requests.get(URL).json()
        if not response["items"]:
            print("error")
            return "error"
        else:
            print(response)
            return response
    except Exception as e:
        return f"Error: {e}"

#### GET LIKE COUNT IN RESPONSE
def make_like_count_request(video_id):
    URL = f"https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails,"  + \
        f"statistics"  + \
        f"&id={video_id}&maxResults=50&" + \
        f"key={API_KEY}"
        #f"status,"  
        #f"topicDetails,"
    response = requests.get(URL).json()
    try:
        likeCountResponse = response["items"][0]["statistics"]["likeCount"]
        return likeCountResponse
    except Exception as e:
        return f"Error: {e}"

#### GET VIEW COUNT IN RESPONSE
def make_view_count_request(video_id): 
    URL = f"https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails,"  + \
        f"statistics"  + \
        f"&id={video_id}&maxResults=50&" + \
        f"key={API_KEY}"
        #f"status,"  
        #f"topicDetails,"
    response = requests.get(URL).json()
    try:
        if 'items' in response and len(response['items']) > 0:
            viewCountResponse = response["items"][0]["statistics"]["viewCount"]
            return viewCountResponse
        else:
            return "Error: No items found in the response"
    except Exception as e:
        return f"Error: {e}"

def make_comment_count_request(video_id):
    URL = f"https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails,"  + \
        f"statistics"  + \
        f"&id={video_id}&maxResults=50&" + \
        f"key={API_KEY}"
        #f"status,"  
        #f"topicDetails,"
    response = requests.get(URL).json()
    try:
        if 'items' in response and len(response['items']) > 0:
            commentCountResponse = response["items"][0]["statistics"]["commentCount"]
            return commentCountResponse
    except Exception as e:
        return f"Error: {e}"
