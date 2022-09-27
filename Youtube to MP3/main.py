import os
from pytube import YouTube

# Aller chercher la vidéo
yt = YouTube(
    'https://www.youtube.com/watch?v=ECkxzFgbJqQ&list=PLxf0dGwBxP3FsWqlEzdKck1Wcb3H7t1dQ'
)

# extraire l'audio
video = yt.streams.get_audio_only()

# dossier ou va se télécharger la music
destination = "../Song"

# téléchargement de la musique
out_file = video.download(output_path=destination)

# enregistrer le fichier
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)
