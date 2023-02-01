from PIL import Image
from pygame import mixer
import window
import room
import user
import customtkinter
from mutagen.mp3 import MP3
import list_user
import list_song

playlist_modif = []
playlist = []
name_song = []

i = 0


class AdminMainWindow(window.Window):

    def __init__(self, room_name, room_password, username, *args, **kwargs):
        super(AdminMainWindow, self).__init__(*args, **kwargs)

        self.database = self.master.database
        self.user = user.User(self.database, username)
        self.room = room.Room(self.database, name=room_name, password=room_password, creator=self.user)

        self.user.change_room(self.room)
        self.room.add_user(user)
        self.database.add_room(self.room)
        self.database.add_user(self.user)

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

        for file in self.master.database.recup_song(room=self.master.room):
            playlist.append(file)
        mixer.music.load(playlist[0])
        mixer.music.play()

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

        for file in range(len(playlist)):
            name_song.append(playlist[file].lstrip('Song/'))

        self.grid_columnconfigure(0, weight=1)

        self.appearance_mode_button = customtkinter.CTkOptionMenu(master=self, values=["dark", "light", "system"],
                                                                  command=self.appearance_mode_button_callback,
                                                                  font=("Courrier", 20))
        self.appearance_mode_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # slider à changer de place (mon opinion)
        # self.name_slider = customtkinter.CTkLabel(master=self, text='Volume',text_color='white',font=("",16))
        # self.name_slider.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.slider = customtkinter.CTkSlider(master=self, command=self.slider_event_volume, progress_color='red')
        self.slider.grid(row=1, column=0, padx=10, pady=20, sticky="nsew")

        self.list_user_button = customtkinter.CTkButton(master=self, command=self.open_list_user, text="List User",
                                                        font=("Courrier", 20))
        self.list_user_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.list_song_button = customtkinter.CTkButton(master=self, command=self.open_list_song, text="List Song",
                                                        font=("Courrier", 20))
        self.list_song_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")



    @staticmethod
    def appearance_mode_button_callback(value):
        customtkinter.set_appearance_mode(value)

    def choix_musique_button(self, value):
        global i
        if value == "i j savais.mp3":
            value = 'Si j savais.mp3'
        i = playlist.index('Song/' + value)
        mixer.music.load(playlist[i])
        mixer.music.play()
        if i == len(playlist) - 2:
            mixer.music.queue(playlist[i + 1])
        else:
            mixer.music.queue(playlist[0])
        self.master.main_frame.song_label.configure(text=name_song[i].lstrip('Song/'))

    @staticmethod
    def slider_event_volume(value):
        mixer.music.set_volume(value)

    def open_list_user(self):
        list_user.ListUser(database=self.master.database, room=self.master.room, admin=True, height=480, width=720)

    def open_list_song(self):
        list_song.ListSong(database=self.master.database, room=self.master.room, user=self.master.user, admin=True,
                           height=480, width=720)


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

        # self.progress_bar = customtkinter.CTkProgressBar(master=self,mode='determinate',
        #                                                  determinate_speed=float(
        #                                                       self.set_duration(playlist[i]))/100.0
        #                                                  )

        # self.progress_bar.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="nsew")
        # self.progress_bar.start()

        self.slider = customtkinter.CTkSlider(master=self, command=self.slider_event)
        self.slider.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="nsew")

    def pause_button_callback(self):
        self.pause_button.grid_forget()
        self.play_button.grid(row=0, column=1, padx=(10, 0), pady=10, sticky="nsew")
        mixer.music.pause()

    def play_button_callback(self):
        self.play_button.grid_forget()
        self.pause_button.grid(row=0, column=1, padx=(10, 0), pady=10, sticky="nsew")
        mixer.music.unpause()

    def back_button_callback(self):
        global i, playlist_modif
        if i > 0:
            i -= 1
        else:
            i = len(playlist) - 1

        playlist_modif = self.Maj_playlist()
        mixer.music.load(playlist_modif[i])
        mixer.music.play()
        if i > 0:
            mixer.music.queue(playlist_modif[i - 1])
            print(playlist_modif[i - 1])
        else:
            mixer.music.queue(playlist_modif[len(playlist_modif)-1])
            print(playlist_modif[len(playlist_modif)-1])
        self.master.song_label.configure(text=playlist_modif[i].lstrip('Song/'))

    def next_button_callback(self):
        global i, playlist_modif
        if i < len(playlist) - 1:
            i += 1
        else:
            i = 0
        playlist_modif = self.Maj_playlist()
        mixer.music.load(playlist_modif[i])
        mixer.music.play()
        if i < len(playlist) - 1:
            mixer.music.queue(playlist_modif[i + 1])
            print(f"Prochaine musique : {playlist_modif[i + 1]}")
        else:
            mixer.music.queue(playlist_modif[0])
            print(f"Prochaine musique : {playlist_modif[0]}")
        self.master.song_label.configure(text=playlist_modif[i].lstrip('Song/'))

    def slider_event(self, value):
        print('On est a ', value * float(self.set_duration(playlist[i])), ' min')

    @staticmethod
    def set_duration(song):
        def audio_duration(duration):
            mins = duration // 60
            duration %= 60
            sec = duration

            return mins, sec

        audio = MP3(song + '')
        audio_info = audio.info
        length = int(audio_info.length)
        minutes, seconds = audio_duration(length)
        tuple_ = (minutes, seconds)
        time = ".".join(map(str, tuple_))
        return time

    def Maj_playlist(self):
        global playlist
        playlist = self.master.master.database.recup_vote_and_song(room=self.master.master.room)
        return playlist


class InfoUser(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super(InfoUser, self).__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.name_slider = customtkinter.CTkLabel(master=self, text='Volume', text_color='white', font=("", 16))
        self.name_slider.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
