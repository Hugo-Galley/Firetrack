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
    video = yt.streams.filter(only_audio=True).first()

    # dossier ou va se télécharger la music
    destination = "Song"

    # téléchargement de la musique
    out_file = video.download(output_path=destination)

    # enregistrer le fichier
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

def add_video(artist,music):
    download_video(research(artist,music))
