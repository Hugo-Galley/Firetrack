import os
from pytube import YouTube
import urllib.request
import re
import tkinter as tk
import sqlite3 as sqltor
import operator
import pygame
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
        master.destroy()
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
        master.destroy()
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

def create_table():
    conn = sqltor.connect("Data Base/user.db")
    cur = conn.cursor()
    cur.execute("""DELETE FROM user_men """)

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS user_men (
	user TEXT,
	nbr_vote INTEGER
	nom TEXT);
	
	
    """)
    conn.commit()
    conn.close()

def add_user(nom):

    conn = sqltor.connect("Data Base/user.db")
    cur = conn.cursor()
    donné = (nom,0)
    conn.execute("INSERT INTO user_men (user,nbr_vote) VALUES (?, ?)",donné)
    conn.commit()
    conn.close()

create_table()
def lecteur_musqiue():
    import pygame
    import playlist_fonction
    import tkinter as tk

    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption("Firetracker")
    screen = pygame.display.set_mode((500, 300))

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

    add_button = pygame.image.load('assets/add.png')
    add_button_rect = add_button.get_rect()
    add_button_rect.x = 20
    add_button_rect.y = 10

    premium_button = pygame.image.load('assets/premium_icon.png')
    premium_button_rect = premium_button.get_rect()
    premium_button_rect.x = 430
    premium_button_rect.y = 10

    running = True
    action = False
    start = False
    premium = False
    playlist = list()
    for i in playlist_fonction.recup():
        playlist.append(i)

    while running:

        screen.blit(background, (0, 0))
        screen.blit(precedent_button, precedent_button_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(pause_button, pause_button_rect)
        screen.blit(next_button, next_button_rect)
        screen.blit(like_button, like_button_rect)
        screen.blit(dislike_button, dislike_button_rect)
        screen.blit(add_button, add_button_rect)
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
                        TEXTE = "Nombre de swipe épuisé veuillez souscire à l'abonnement premium"
                        label = tk.Label(win, text=TEXTE,
                                         wraplength=(100),
                                         justify=tk.CENTER)
                        label.pack()
                        win.mainloop()
                    elif i < len(playlist) - 2:
                        i += 1
                        pygame.mixer.music.load(playlist[i])
                        pygame.mixer.music.play()
                        pygame.mixer.music.queue(playlist[i + 1])





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
                        TEXTE = "Nombre de swipe épuisé veuillez souscire à l'abonnement premium"
                        label = tk.Label(win, text=TEXTE,
                                         wraplength=(100),
                                         justify=tk.CENTER)
                        label.pack()
                        win.mainloop()
                    elif i > 0:
                        i -= 1
                        pygame.mixer.music.load(playlist[i])
                        pygame.mixer.music.play()
                        pygame.mixer.music.queue(playlist[i - 1])



                    else:
                        i = len(playlist[i]) - 1
                        pygame.mixer.music.load(playlist[i])
                        pygame.mixer.music.play()
                        pygame.mixer.music.queue(playlist[i - 1])

                    print(playlist[i])

                elif like_button_rect.collidepoint(event.pos):
                    playlist_fonction.add_vote(playlist[i], True)
                    playlist = playlist_fonction.recup_vote_and_song()



                elif dislike_button_rect.collidepoint(event.pos):
                    playlist_fonction.add_vote(playlist[i], False)
                    playlist = playlist_fonction.recup_vote_and_song()


                elif add_button_rect.collidepoint(event.pos):
                    # playlist_fonction.menu_deroulant()

                    win = tk.Tk()
                    TEXTE = "Fonction en phase de test, bientôt disponible"
                    label = tk.Label(win, text=TEXTE,
                                     wraplength=(80),
                                     justify=tk.CENTER)
                    label.pack()
                    win.mainloop()

                    # playlist_fonction.add_video(playlist_fonction.choix_artiste(), playlist_fonction.choix_music())
                elif premium_button_rect.collidepoint(event.pos):
                    premium = True
                    win = tk.Tk()
                    win.geometry('200x100')
                    TEXTE = "Merci d'avoir souscris à notre offre premium"
                    label = tk.Label(win, text=TEXTE,
                                     wraplength=(70),
                                     justify=tk.CENTER)
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
