import os
from pytube import YouTube
import urllib.request
import re

def research(artist,music):
    artist =artist
    music = music
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + artist + music)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    link = ("https://www.youtube.com/watch?v=" + video_ids[0])

    return link

def download_video(link):
    # Aller chercher la vidéo
    yt = YouTube(
        link
    )

    # extraire l'audio
    video = yt.streams.filter(file_extension="mp3",only_audio=True)


    # dossier ou va se télécharger la music
    destination = "Song"

    # téléchargement de la musique
    video.download(output_path=destination)




def add_video(artist,music):
    download_video(research(artist,music))
add_video('gazo','die')
