import os
from pytube import YouTube
import urllib.request
import re
import tkinter as tk
import sqlite3 as sqltor
import operator
def research(artist,music):
    artist =artist
    music = music
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + artist + music)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    link = ("https://www.youtube.com/watch?v=" + video_ids[0])

    return link

def download_video(link):
    # extract only audio
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    destination = "Song"

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
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

    tk.Button(master, text='Add', command=show_entry_fields).grid(row=3,
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

    tk.Button(master, text='Add', command=show_entry_fields).grid(row=3,
                                                                   column=1,
                                                                   sticky=tk.W,
                                                                   pady=4)

    master.mainloop()
    return show_entry_fields()

def recup():
    file_list = os.listdir("Song")
    f = len(file_list)

    connexion = sqltor.connect("Data Base/Songs.db")

    curseur = connexion.cursor()
    curseur.execute(""" DELETE FROM 'playlist' """)

    curseur.executescript("""

        CREATE TABLE IF NOT EXISTS playlist(
        id_titre INTEGER PRIMARY KEY,
        titre TEXT,
        integer vote );

       """)
    i = 0
    donnees_liste = []
    playlist = []
    for fichier in range(len(file_list)):
        i = i + 1
        j = 0
        file_list[fichier] = 'Song/' + file_list[fichier]
        playlist.append(file_list[fichier])
        donnees_liste.append((file_list[fichier], j))


    curseur.executemany("INSERT INTO playlist (titre,vote) VALUES (?, ?)", donnees_liste)

    connexion.commit()

    connexion.close()
    return playlist
def add_vote(name,like):
    ### SQL
    conn = sqltor.connect('Data Base/Songs.db')
    cursor = conn.cursor()
    pd =sqltor.connect("Data Base/Songs.db")
    if like:
        command = 'update playlist set vote=vote+1 where titre=?'
    else :
        command = 'update playlist set vote=vote-1 where titre=?'
    pd.execute(command,(name,))
    pd.commit()
    win = tk.Tk()
    TEXTE = "Merci d'avoir votée"
    label = tk.Label(win, text=TEXTE,
                     wraplength=(50),
                     justify=tk.CENTER)
    label.pack()
    win.mainloop()

def recup_vote_and_song():
    song_playlist_trié=[]
    conn = sqltor.connect('Data Base/Songs.db')
    cur = conn.cursor()
    cur.execute("""SELECT titre,vote FROM playlist""")
    result = cur.fetchall()
    playlist_triée = sorted(result, key=operator.itemgetter(1),reverse=True)
    for i in range(len(playlist_triée)):
        song_playlist_trié.append(playlist_triée[i][0])
    return song_playlist_trié


def menu_deroulant():
    player = tk.Tk()
    player.title("Playlist")
    player.geometry("205x400")
    os.chdir("Song")

    songlist = os.listdir()
    playlist = tk.Listbox(player)
    for item in songlist:
        pos = 0
        playlist.insert(pos, item)
        pos = pos + 1
    playlist.pack(fill="both", expand="yes")
    player.mainloop()
recup()
