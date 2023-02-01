import operator
import os
import pygame
import re
import sqlite3 as sqltor
import tkinter as tk
import urllib.request
from pytube import YouTube
import time
import tkinter.filedialog
from mutagen.mp3 import MP3
import functools
import moviepy as mp


# Choix artiste
def research(music):
    artist = ''
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + music + artist)
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

    my_clip = mp.VideoFileClip(os.path.abspath(out_file))

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'

    my_clip.audio.write_audiofile(new_file)
    my_clip.close()

    os.remove(out_file)


def add_video(music):
    download_video(str(music))


def choix_music():
    music = ''
    def show_entry_fields():
        music = e2.get()
        print(music)
        master.destroy()


    master = tk.Tk()
    tk.Label(master, text="Music ").grid(row=1)

    e2 = tk.Entry(master)

    e2.grid(row=1, column=1)

    tk.Button(master, text='Add', command=show_entry_fields).grid(row=3,
                                                                  column=1,
                                                                  sticky=tk.W,
                                                                  pady=4)

    master.mainloop()
    return music


# recuperation contenue SQL
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
        integer vote);

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
        print(donnees_liste)

    curseur.executemany("INSERT INTO playlist (titre,vote) VALUES (?, ?)", donnees_liste)

    connexion.commit()

    connexion.close()
    return playlist


def add_vote(name, like):
    # SQL
    conn = sqltor.connect('Data Base/Songs.db')
    cursor = conn.cursor()
    pd = sqltor.connect("Data Base/Songs.db")
    if like:
        command = 'update playlist set vote=vote+1 where titre=?'
    else:
        command = 'update playlist set vote=vote-1 where titre=?'
    pd.execute(command, (name,))
    pd.commit()
    win = tk.Tk()
    texte = "Merci d'avoir votée"
    label = tk.Label(win, text=texte,
                     wraplength=50,
                     justify=tk.CENTER)
    label.pack()
    win.mainloop()


def recup_vote_and_song():
    song_playlist_trie = []
    conn = sqltor.connect('Data Base/Songs.db')
    cur = conn.cursor()
    cur.execute("""SELECT titre,vote FROM playlist""")
    result = cur.fetchall()
    playlist_triee = sorted(result, key=operator.itemgetter(1), reverse=True)
    for i in range(len(playlist_triee)):
        song_playlist_trie.append(playlist_triee[i][0])
    return song_playlist_trie


def create_table():
    conn = sqltor.connect("Data Base/user.db")
    cur = conn.cursor()
    cur.execute("""DELETE FROM user_men """)

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS user_men (user TEXT PRIMARY KEY, nbr_vote INTEGER,premium INTEGER);
    """)
    conn.commit()
    conn.close()


def add_user(nom):
    conn = sqltor.connect("Data Base/user.db")
    cur = conn.cursor()
    donne = (nom, 0, 0)
    conn.execute("INSERT INTO user_men (user,nbr_vote,premium) VALUES (?, ?,?)", donne)
    conn.commit()
    conn.close()


def add_user_vote(name, like):
    # SQL
    conn = sqltor.connect("Data Base/user.db")
    if like:
        command = 'update user_men set nbr_vote=nbr_vote+1 where user=(?)'
    else:
        command = 'update user_men set nbr_vote=nbr_vote-1 where user=(?)'
    conn.execute(command, (name,))
    conn.commit()
    conn.close()


def add_premium(name):
    conn = sqltor.connect('Data Base/user.db')
    command = 'update user_men set premium=premium+1 where user=(?)'
    conn.execute(command, (name,))
    conn.commit()
    conn.close()


def info_premium(nom):
    conn = sqltor.connect('Data Base/user.db')
    cur = conn.cursor()
    cur.execute("""SELECT premium FROM user_men WHERE user = (?)""", [nom])
    result = cur.fetchall()
    conn.close()
    return result


def recup_info_user(nom):
    conn = sqltor.connect('Data Base/user.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM user_men WHERE user = (?) """, [nom])
    result = cur.fetchall()
    conn.close()

    return result


def add_room(num, username):
    conn = sqltor.connect("Data Base/room.db")
    cur = conn.cursor()
    donne = (num, username)
    conn.execute("INSERT INTO room (num_room, user) VALUES (?, ?)", donne)
    conn.commit()
    conn.close()




def menu_deroulant():
    player = tk.Tk()
    player.title("Playlist")
    player.geometry("205x400")

    song = os.listdir("Song")
    songlist = []
    for i in song:
        i = "Song/" + i
        songlist.append(i)

    playlist = tk.Listbox(player, highlightcolor="blue", selectmode=tk.SINGLE)
    pos = 0
    for item in songlist:
        playlist.insert(pos, item)
        pos = pos + 1
    playlist.pack(fill="both", expand="yes")
    var = playlist.get(tk.ACTIVE)
    player.mainloop()

    return var


def lecteur_musique():
    pygame.init()
    pygame.mixer.init()
    icon = pygame.image.load('assets/logo.png')

    pygame.display.set_caption("Firetracke", "Spotify")
    screen = pygame.display.set_mode((500, 300))
    pygame.display.set_icon(icon)

    background = pygame.image.load("assets/background.jpg")

    play_button = pygame.image.load("assets/play_button.png")
    play_button_rect = play_button.get_rect()
    play_button_rect.x = 200
    play_button_rect.y = 110

    pause_button = pygame.image.load("assets/pause_buton.png")
    pause_button_rect = pause_button.get_rect()
    pause_button_rect.x = 300
    pause_button_rect.y = 110

    next_button = pygame.image.load("assets/next_button.png")
    next_button_rect = next_button.get_rect()
    next_button_rect.x = 400
    next_button_rect.y = 110

    precedent_button = pygame.image.load('assets/precedent_button.png')
    precedent_button_rect = precedent_button.get_rect()
    precedent_button_rect.x = 100
    precedent_button_rect.y = 110

    like_button = pygame.image.load('assets/like.png')
    like_button_rect = like_button.get_rect()
    like_button_rect.x = 50
    like_button_rect.y = 190

    dislike_button = pygame.image.load('assets/dislike.png')
    dislike_button_rect = dislike_button.get_rect()
    dislike_button_rect.x = 450
    dislike_button_rect.y = 200

    menu_button = pygame.image.load('assets/menu.png')
    menu_button_rect = menu_button.get_rect()
    menu_button_rect.x = 20
    menu_button_rect.y = 10

    premium_button = pygame.image.load('assets/premium_icon.png')
    premium_button_rect = premium_button.get_rect()
    premium_button_rect.x = 430
    premium_button_rect.y = 10

    running = True
    action = False
    start = False
    premium = False
    playlist = list()
    for i in recup():
        playlist.append(i)

    while running:

        screen.blit(background, (0, 0))
        screen.blit(precedent_button, precedent_button_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(pause_button, pause_button_rect)
        screen.blit(next_button, next_button_rect)
        screen.blit(like_button, like_button_rect)
        screen.blit(dislike_button, dislike_button_rect)
        screen.blit(menu_button, menu_button_rect)
        screen.blit(premium_button, premium_button_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if play_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.unpause()
                    action = False
                    print("play")

                elif pause_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.pause()
                    action = True
                    print("pause")
                elif next_button_rect.collidepoint(event.pos):
                    if i == 5 and not premium:
                        win = tk.Tk()
                        win.geometry('200x100')
                        texte = "Nombre de swipe épuisé veuillez souscire à l'abonnement premium"
                        label = tk.Label(win, text=texte, wraplength=100, justify=tk.CENTER)
                        label.pack()
                        win.mainloop()
                    elif i < len(playlist) - 2:
                        i += 1
                        pygame.mixer.music.load(playlist[i])
                        pygame.mixer.music.play()
                        pygame.mixer.music.queue(playlist[i + 1])
                        print(playlist[i])

                    else:
                        i = 0
                        pygame.mixer.music.load(playlist[i])
                        pygame.mixer.music.play()
                        pygame.mixer.music.queue(playlist[i + 1])
                        print(playlist[i])

                elif precedent_button_rect.collidepoint(event.pos):
                    if i == 5 and not premium:
                        win = tk.Tk()
                        win.geometry('200x100')
                        texte = "Nombre de swipe épuisé veuillez souscire à l'abonnement premium"
                        label = tk.Label(win, text=texte, wraplength=100, justify=tk.CENTER)
                        label.pack()
                        win.mainloop()
                    elif i > 0:
                        i -= 1
                        pygame.mixer.music.load(playlist[i])
                        pygame.mixer.music.play()
                        pygame.mixer.music.queue(playlist[i - 1])
                        print(playlist[i])

                    else:
                        i = len(playlist[i]) - 1
                        pygame.mixer.music.load(playlist[i])
                        pygame.mixer.music.play()
                        pygame.mixer.music.queue(playlist[i - 1])
                        print(playlist[i])

                elif like_button_rect.collidepoint(event.pos):
                    add_vote(playlist[i], True)
                    playlist = recup_vote_and_song()

                elif dislike_button_rect.collidepoint(event.pos):
                    add_vote(playlist[i], False)
                    playlist = recup_vote_and_song()

                elif menu_button_rect.collidepoint(event.pos):

                    ouvrir_fichier = tkinter.filedialog.askopenfilename(title="Ouvrir un fichier",defaultextension=".mp3",filetypes=[("txt fichier", ".mp3")])
                    playlist.append(ouvrir_fichier)
                    pygame.mixer.music.load(ouvrir_fichier)
                    pygame.mixer.music.queue(ouvrir_fichier)
                    pygame.mixer.music.play()

                    #pygame.mixer.music.queue(menu_deroulant())

                    # win = tk.Tk()
                    # texte = "Fonction en phase de test, bientôt disponible"
                    # label = tk.Label(win, text=texte, wraplength=80, justify=tk.CENTER)
                    # label.pack()
                    # win.mainloop()


                    #add_video(choix_music())
                elif premium_button_rect.collidepoint(event.pos):
                    if not premium:
                        def return_entry():
                            add_premium(enter.get())
                            win.destroy()
                            return

                        win = tk.Tk()
                        win.geometry('200x100')
                        label = tk.Label(win, text="Nom d'user", wraplength=100, justify=tk.CENTER)
                        label.pack()
                        enter = tk.Entry(win)
                        enter.pack()
                        tk.Button(win, text='Add', font=("Courier", 8), command=return_entry).pack()
                        texte = "Merci d'avoir souscris à notre offre premium"
                        win.mainloop()
                    else:
                        texte = "Vous possedez deja l'offre premium"

                    premium = True
                    win = tk.Tk()
                    win.geometry('200x100')
                    label = tk.Label(win, text=texte, wraplength=70, justify=tk.CENTER)
                    label.pack()
                    win.mainloop()

            if not action and not start:
                for song in range(len(playlist)):
                    i = 0
                    pygame.mixer.music.load(playlist[song])
                    pygame.mixer.music.play()
                    print("Loading song ...")
                    start = True
                print("Votre playlist contient : ", len(playlist), " morceaux")
