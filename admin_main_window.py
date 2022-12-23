import time

from PIL import Image

import customtkinter
import pygame
import tkinter.filedialog

import window
import database
from mutagen.mp3 import MP3

playlist_modif = []
playlist = []
name_song = []

global i
i = 0

class AdminMainWindow(window.Window):

    def __init__(self, room_name, room_password, username, *args, **kwargs):
        super(AdminMainWindow, self).__init__(*args, **kwargs)

        #self.user = user.User(username)
        #self.room = room.Room(name=room_name, password=room_password, creator=self.user)
        #self.database = database.DataBase()

        #self.user.change_room(self.room)
        #self.room.add_user(user)
        #self.database.add_room(self.room)
        #self.database.add_user(self.user)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.menu_frame_state = False

        self.main_frame = MainFrame(master=self)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.menu_frame = MenuFrame(master=self)

    def open_menu(self):
        if not self.menu_frame_state:
            self.menu_frame.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsew")
            self.menu_frame_state = True
            return
        self.menu_frame.grid_forget()
        self.menu_frame_state = False


class MainFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        for fichier in database.DataBase.recup_song():
            playlist.append(fichier)
        pygame.mixer.music.load(playlist[0])
        pygame.mixer.music.play()

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.song_label = customtkinter.CTkLabel(master=self, text=playlist[i].lstrip('../Song/ '),
                                                 font=("Courrier", 30))
        self.song_label.grid(row=0, rowspan=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.menu_button_image = customtkinter.CTkImage(light_image=Image.open("assets/menu_dark_mode.png"),
                                                        dark_image=Image.open("assets/menu_light_mode.png"),
                                                        size=(50, 50))

        self.menu_button = customtkinter.CTkButton(master=self, image=self.menu_button_image, text="", width=50,
                                                   height=50, fg_color="transparent",
                                                   command=self.master.open_menu)
        self.menu_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.music_params = MusicParams(master=self)
        self.music_params.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


class MenuFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(MenuFrame, self).__init__(*args, **kwargs)

        for fichier in range(len(playlist)):
            name_song.append(playlist[fichier].lstrip('Song/'))

        self.grid_columnconfigure(0, weight=1)

        self.appearance_mode_button = customtkinter.CTkOptionMenu(master=self, values=["dark", "light", "system"],
                                                                  command=self.appearance_mode_button_callback)
        self.appearance_mode_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # slider à changer de place (mon opinion)
        self.name_slider = customtkinter.CTkLabel(master=self, text='Volume',text_color='white',font=("",16))
        self.name_slider.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.slider = customtkinter.CTkSlider(master=self, command= self.slider_event_volume,progress_color='red')
        self.slider.grid(row=2, column=0, padx=10, pady=20, sticky="nsew")

        # bouton like et dislike (à débattre)
        self.upvote_image_button = customtkinter.CTkImage(light_image=Image.open('assets/like_light_mode.png'),
                                                          dark_image=Image.open('assets/like_dark_mode.png'),
                                                          size= (50,50))

        self.upvote_button = customtkinter.CTkButton(master=self, image=self.upvote_image_button,width=10,height=10,
                                                     fg_color='transparent',text='',command=self.upvote)
        self.upvote_button.grid(row=3, column=0, padx=10, pady=20, sticky='nsew')

        self.downvote_button_image = customtkinter.CTkImage(light_image=Image.open('assets/dislike_light_mode.png'),
                                                            dark_image=Image.open('assets/dislike_dark_mode.png'),
                                                            size=(30,30))
        self.downvote_button = customtkinter.CTkButton(master=self, image=self.downvote_button_image, width=10, height=10,
                                                       fg_color='transparent', text='', command=self.downvote)
        self.downvote_button.grid(row=4, column=0, padx=10, pady=20, sticky='nsew')

        self.menu_deroulant = customtkinter.CTkComboBox(master=self, values=name_song,
                                                          command=self.choix_musique_button)
        self.menu_deroulant.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")


    def appearance_mode_button_callback(self, value):
        customtkinter.set_appearance_mode(value)

    def choix_musique_button(self, value):
        global i
        if value == "i j savais.mp3":
            value = 'Si j savais.mp3'
        i = playlist.index('Song/' + value)
        pygame.mixer.music.load(playlist[i])
        pygame.mixer.music.play()
        if i == len(playlist) - 2:
            pygame.mixer.music.queue(playlist[i + 1])
        else:
            pygame.mixer.music.queue(playlist[0])
        self.master.main_frame.song_label.configure(text=name_song[i].lstrip('Song/'))
    def slider_event_volume(self, value):
        pygame.mixer.music.set_volume(value)

    def upvote(self):
        print('add vote')
        database.DataBase.addvote(playlist[i], True)
        self.Maj_playlist()


    def downvote(self):
        print('down vote')
        database.DataBase.addvote(playlist[i], False)
        self.Maj_playlist()

    def Maj_playlist(self):
        playlist = database.DataBase.recup_vote_and_song()
        name_song = []
        for fichier in range(len(playlist)):
            name_song.append(playlist[fichier].lstrip('Song/'))
        self.menu_deroulant.configure(values=name_song)



class MusicParams(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(MusicParams, self).__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.back_button_image = customtkinter.CTkImage(
            light_image=Image.open("assets/precedent_button_light_mode.png"),
            dark_image=Image.open("assets/precedent_button_dark_mode.png")
        )
        self.next_button_image = customtkinter.CTkImage(light_image=Image.open("assets/next_button_light_mode.png"),
                                                        dark_image=Image.open("assets/next_button_dark_mode.png"))
        self.pause_button_image = customtkinter.CTkImage(light_image=Image.open("assets/pause_buton_light_mode.png"),
                                                         dark_image=Image.open("assets/pause_buton_dark_mode.png"))
        self.play_button_image = customtkinter.CTkImage(light_image=Image.open("assets/play_button_light_mode.png"),
                                                        dark_image=Image.open("assets/play_button_dark_mode.png"))

        self.back_button = customtkinter.CTkButton(master=self, image=self.back_button_image, text="", width=40,
                                                   fg_color="transparent", command=self.back_button_callback)
        self.back_button.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsew")

        self.next_button = customtkinter.CTkButton(master=self, image=self.next_button_image, text="", width=40,
                                                   fg_color="transparent", command=self.next_button_callback)
        self.next_button.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")

        self.pause_button = customtkinter.CTkButton(master=self, image=self.pause_button_image, text="", width=40,
                                                    fg_color="transparent", command=self.pause_button_callback)
        self.pause_button.grid(row=0, column=1, padx=(10, 0), pady=10, sticky="nsew")

        self.play_button = customtkinter.CTkButton(master=self, image=self.play_button_image, text="", width=40,
                                                   fg_color="transparent", command=self.play_button_callback)

        #self.progress_bar = customtkinter.CTkProgressBar(master=self,mode='determinate',determinate_speed=float(self.set_duration(playlist[i]))/100.0)

        #self.progress_bar.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="nsew")
        #self.progress_bar.start()

        self.slider = customtkinter.CTkSlider(master=self, command=self.slider_event)
        self.slider.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="nsew")

    def pause_button_callback(self):
        self.pause_button.grid_forget()
        self.play_button.grid(row=0, column=1, padx=(10, 0), pady=10, sticky="nsew")
        pygame.mixer.music.pause()

    def play_button_callback(self):
        self.play_button.grid_forget()
        self.pause_button.grid(row=0, column=1, padx=(10, 0), pady=10, sticky="nsew")
        pygame.mixer.music.unpause()

    def back_button_callback(self):
        global i
        if i > 0:
            i -= 1
        else:
            i = len(playlist) - 1

        playlist_modif = self.Maj_playlist()
        pygame.mixer.music.load(playlist_modif[i])
        pygame.mixer.music.play()
        if i > 0:
            pygame.mixer.music.queue(playlist_modif[i - 1])
            print(playlist_modif[i - 1])
        else :
            pygame.mixer.music.queue(playlist_modif[len(playlist_modif)])
            print(playlist_modif[len(playlist_modif)])
        self.master.song_label.configure(text=playlist_modif[i].lstrip('Song/'))

    def next_button_callback(self):
        global i
        if i < len(playlist) - 1:
            i += 1
        else:
            i = 0
        playlist_modif = self.Maj_playlist()
        pygame.mixer.music.load(playlist_modif[i])
        pygame.mixer.music.play()
        if i < len(playlist) - 1:
            pygame.mixer.music.queue(playlist_modif[i + 1])
            print(playlist_modif[i + 1 ])
        else :
            pygame.mixer.music.queue(playlist_modif[0])
            print(playlist_modif[0])
        self.master.song_label.configure(text=playlist_modif[i].lstrip('Song/'))


    def slider_event(self, value):
        print('On est a ',value * float(self.set_duration(playlist[i])),' min')

    def set_duration(self, song):
        def audio_duration(length):
            mins = length // 60
            length %= 60
            seconds = length

            return mins, seconds

        audio = MP3(song + '')
        audio_info = audio.info
        length = int(audio_info.length)
        mins, seconds = audio_duration(length)
        tuple = (mins, seconds)
        time = ".".join(map(str, tuple))
        return time

    def Maj_playlist(self):
        playlist = database.DataBase.recup_vote_and_song()
        return playlist