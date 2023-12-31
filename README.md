<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="![image](https://github.com/MohamedMrj/YoutubeAPI_GUI/assets/113178714/280de505-43de-4e43-82f9-58954f3eb1ff)
" alt="Project logo"></a>
</p>

<h3 align="center">Youtube API GUI</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> This project helps users to get information about a youtube channel or a youtube video.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

With help of tkinter library and Youtube API, I made a Graphical User Interface to pull data from Youtube. This data can be video related such as comments count, views count, and even like count. 
With this program you can also get Youtube Channel ID for any youtube channel just by simple pasting the link in the relevant field. 
You can also pull data related to a youtube channel of your choice and this data can be that last 50 videos a channel published and their publishing date. 
I enjoyed this project a lot and I have plansfor further improvements and features.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
- Install Python 3.11 or above
- Install requests (pip install requests)
- Install tkinter (pip install tk) more info here (https://www.tutorialspoint.com/how-to-install-tkinter-in-python)
- Import json (import json)
- Install pytube (pip install pytube) more info here (https://pytube.io/en/latest/user/install.html)
- Grab your API Key from https://developers.google.com/youtube/v3/getting-started 
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Make sure to have Python 3.11 or above.

```
Download python from https://www.python.org/downloads/
```

Install requests

```
Requests is a simple, yet elegant, HTTP library
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!

Requests is one of the most downloaded Python packages today, pulling in around 30M downloads / week— according to GitHub, Requests is currently depended upon by 1,000,000+ repositories. You may certainly put your trust in this code.

You can install it by:

pip install requests
or 
python -m pip install requests
```

End with an example of getting some data out of the system or using it for a little demo.


## 🎈 Usage <a name="usage"></a>

Make sure to paste your API KEY in API>api.py
You can use this application by getting a youtube video channel link or ID directly to put it in the relevant fields and then click on buttons

![API GUI MAIN](image.png)
![paste youtube channel url](image-1.png)
![Click on COPY ID](image-2.png)
![Click on SHOW ID](image-3.png)
![Paste channel ID](image-4.png)
![Response message after we click on videos and publishing dates](image-5.png)
![get comments count for a specific video](image-6.png)
![Get likes count for a specific video](image-7.png)
![Get views count for a specific video](image-8.png)
![Initial system design skiss for the system](image-9.png)


## 🚀 Deployment <a name = "deployment"></a>

Optional: You can launch this in a virtual enviroment

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org//) - Python
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Tkinter
- [Pytube](https://pytube.io/en/latest/) - Pythube
- [Youtube Data API](https://developers.google.com/youtube/v3/docs/search/list) - Youtube Data API

## ✍️ Authors <a name = "authors"></a>

- [@Mohamedmrj](https://github.com/MohamedMrj) - Idea & Initial work

See also the list of [contributors](https://github.com/MohamedMrj/) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Thanks to @athiyadeviyani for creating this cheat sheet https://gist.github.com/athiyadeviyani/b18afdc8136f003956b1a71d94a6c696 which helped a lot!
