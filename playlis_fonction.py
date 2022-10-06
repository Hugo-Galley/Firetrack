import os
import sqlite3
from pytube import YouTube
import urllib.request
import re
import tkinter as tk

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
    video = yt.streams.get_audio_only()


    # dossier ou va se télécharger la music
    destination = "Song"

    # téléchargement de la musique
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

def add_video(artist,music):
    download_video(research(artist,music))

def choix_artiste():
    def show_entry_fields():
        artist = e1.get()

        master.quit()
        return artist

    master = tk.Tk()
    tk.Label(master, text="Artist ").grid(row=0)


    e1 = tk.Entry(master)


    e1.grid(row=0, column=1)

    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master, text='Show', command=show_entry_fields).grid(row=3,
                                                                   column=1,
                                                                   sticky=tk.W,
                                                                   pady=4)

    master.mainloop()
    return show_entry_fields()

def choix_music():
    def show_entry_fields():
        music = e2.get()
        master.quit()
        return music

    master = tk.Tk()
    tk.Label(master, text="Music ").grid(row=1)

    e2 = tk.Entry(master)


    e2.grid(row=1, column=1)

    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master, text='Show', command=show_entry_fields).grid(row=3,
                                                                   column=1,
                                                                   sticky=tk.W,
                                                                   pady=4)

    master.mainloop()
    return show_entry_fields()

def recup():
    file_list = os.listdir("Song")
    f = len(file_list)
    print(f, "fichiers trouvés dans le dossier")

    connexion = sqlite3.connect("Data Base/donné_musique.db")

    curseur = connexion.cursor()

    curseur.executescript("""

        CREATE TABLE IF NOT EXISTS playlist(
        id_titre INTEGER PRIMARY KEY,
        titre TEXT,
        integer vote);

       """)
    i = 0
    donnees_liste = []
    playlist = []
    for fichier in range(len(file_list)):
        i = i + 1
        file_list[fichier] = 'Song/' + file_list[fichier]
        playlist.append(file_list[fichier])

    print(i, "fichiers préparés pour la base")

    curseur.executemany("INSERT INTO playlist (titre,vote) VALUES (?, ?)", donnees_liste)

    connexion.commit()

    connexion.close()
    return playlist

