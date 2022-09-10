from pytube import YouTube
from pathlib import Path
from youtube_dl import YoutubeDL
import os
from pytube.cli import on_progress

fuchsia = '\033[38;2;255;00;255m'  # color as hex #FF00FF
reset_color = '\033[39m'

import progressbar as on_progress

downloads_path = str(Path.home() / "Downloads")

print("A YouTube video downloader by Bharath Prakash")
str = input("Enter \n 'a' for audio downlaoder   \n 'v' for video downloader  \n 'e' for exit \n enter the command :  ")

class Youtubeaud:
    def __init__(self):

        print("WELCOME TO THE YOUTUBE VIDEO DOWNLOADER")
        ytlink=input("Enter the youtube link ->\npaste here : ")
        print("***********Youtube audio downloader***************")
        yt = YouTube(ytlink,on_progress_callback=on_progress)
        print("Title : ", yt.title)
        print("Views : ", yt.views)
        print("Author Name : ",yt.author)
        print("length : ", yt.length, "seconds")
        #yt.register_on_progress_callback(progress_function)
        print(f'\n' + fuchsia + 'Downloading: ', yt.title, '~ viewed', yt.views,
              'times.')
        yd=yt.streams.get_by_itag(251)
        download=yd.download(downloads_path)
        print('your file is downloading.........')
        base,ext=os.path.splitext(download)
        newfile=base +'.mp3'
        os.rename(download,newfile)
        print("Download completed\n")



class Youtubevid:
        def __init__(self):

            print("WELCOME TO THE YOUTUBE VIDEO DOWNLOADER")
            ytlink=input("Enter the youtube link ->\npaste here : ")
            print("***********Youtube Video downloader***************")
            yt = YouTube(ytlink,on_progress_callback=on_progress)
            print("Title", yt.title)
            print("View", yt.views)
            print("Author Name : ", yt.author)
            print("Length", yt.length, "seconds")
            print('Your file is downloading.........')
            print("You can minimize this window")
            print(f'\n' + fuchsia + 'Downloading: ', yt.title, '~ viewed', yt.views,
                  'times.')
            #yt.register_on_progress_callback(progress_function)
            yd = yt.streams.get_by_itag(22)
            yf=YoutubeDL({'format':''})
            yd.download('D:\downloads')
            print("Download completed\n","located at ",downloads_path)




try:
    if(str=='a'or str=='A'):
        Youtubeaud()
    elif(str=='v'or str=='V'):
        Youtubevid()
    elif(str=='e'or str=='E'):
        exit()
    else:
        print('please enter the correct argument ')
   
except Exception as e:
    print("An error occured : ",e)