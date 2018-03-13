'''
Created on 13-Mar-2018

@author: akhay
'''
from pytube import YouTube
from pytube import Playlist
import os

videoCode = '9bZkp7q19f0'
playListCode = 'PLd3UqWTnYXOkVR3OR9UZGyEt9RFUbaTMZ'


def download_single_video_using_video_code(video_code):
    constructed_url = 'http://youtube.com/watch?v=' + video_code
    YouTube(constructed_url).streams.first().download()


def download_video_playlist_using_code(video_code):
    constructed_url = 'https://www.youtube.com/playlist?list=' + video_code
    pl = Playlist(constructed_url)
    pl.download_all()


def download_single_video_using_full_url(video_url):
    YouTube(video_url).streams.first().download()


def download_video_playlist_using_full_url(play_list_url):
    pl = Playlist(play_list_url)
    pl.download_all()


def download_video_playlist_using_url_and_save_in_specific_path(play_list_url, path):
    pl = Playlist(play_list_url)
    if not os.path.exists(path):
        os.makedirs(path)
        pl.download_all(path)
    else:
        pl.download_all(path)


def download_single_video_using_full_url_and_save_in_specific_path(video_url, path):
    if not os.path.exists(path):
        os.makedirs(path)
        YouTube(video_url).streams.first().download(path)
    else:
        YouTube(video_url).streams.first().download(path)
        
download_single_video_using_full_url_and_save_in_specific_path('https://www.youtube.com/watch?v=SjDXOVq7oc8', 'D:\\')