import yt_dlp
import tkinter as tk
from tkinter import filedialog
from os import system

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')
    
    return folder

if __name__ == '__main__':
    while True:
        video_url = input('Enter the video url that you want to download: ')
        if 'https://www.youtube.com/' not in video_url:
            print('Please, enter the right url')
        else:
            break    

    output_folder_path = open_file_dialog()

    options = {
        'format' : 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl' : f'{output_folder_path}/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_url])
        print('The video successfully downloaded into your folder')
        
    system('pause')

