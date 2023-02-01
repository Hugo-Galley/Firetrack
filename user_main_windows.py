from PIL import Image
from pygame import mixer
import window
import user
import room
import customtkinter
from mutagen.mp3 import MP3
playlist_modif = []
playlist = []
name_song = []

i = 0


class UserMainWindow(window.Window):

    def __init__(self, room_name, room_password, username, *args, **kwargs):
        super(UserMainWindow, self).__init__(*args, **kwargs)

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

        for fichier in self.master.database.recup_song(self.master.room):
            playlist.append(fichier)
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

        for fichier in range(len(playlist)):
            name_song.append(playlist[fichier].lstrip('Song/'))

        self.grid_columnconfigure(0, weight=1)

        self.appearance_mode_button = customtkinter.CTkOptionMenu(master=self, values=["dark", "light", "system"],
                                                                  command=self.appearance_mode_button_callback)
        self.appearance_mode_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # slider à changer de place (mon opinion)
        self.name_slider = customtkinter.CTkLabel(master=self, text='Volume', text_color='white', font=("", 16))
        self.name_slider.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.slider = customtkinter.CTkSlider(master=self, command=self.slider_event_volume, progress_color='red')
        self.slider.grid(row=1, column=0, padx=10, pady=20, sticky="nsew")

        self.menu_deroulant = customtkinter.CTkComboBox(master=self, values=name_song,
                                                        command=self.choix_musique_button)
        self.menu_deroulant.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")


    @staticmethod
    def appearance_mode_button_callback(value):
        customtkinter.set_appearance_mode(value)

    def choix_musique_button(self, value):
        global i, name_song, playlist
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


class MusicParams(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(MusicParams, self).__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.next_title = customtkinter.CTkLabel(master=self,
                                                 text=f"Next title is : {playlist[i + 1].lstrip('../Song/ ')}",
                                                 font=("Courrier", 20))
        self.next_title.grid(row=0, column=2, padx=10, pady=20, sticky='nsew')

        self.upvote_image_button = customtkinter.CTkImage(light_image=Image.open('assets/like_light_mode.png'),
                                                          dark_image=Image.open('assets/like_dark_mode.png'),
                                                          size=(50, 50))

        self.upvote_button = customtkinter.CTkButton(master=self, image=self.upvote_image_button, width=10, height=10,
                                                     fg_color='transparent', text='', command=self.upvote)
        self.upvote_button.grid(row=0, column=6, padx=10, pady=10, sticky='nsew')

        self.downvote_button_image = customtkinter.CTkImage(light_image=Image.open('assets/dislike_light_mode.png'),
                                                            dark_image=Image.open('assets/dislike_dark_mode.png'),
                                                            size=(30, 30))
        self.downvote_button = customtkinter.CTkButton(master=self, image=self.downvote_button_image, width=10,
                                                       height=10, fg_color='transparent', text='',
                                                       command=self.downvote)
        self.downvote_button.grid(row=0, column=0, padx=10, pady=20, sticky='nsew')


        # self.progress_bar = customtkinter.CTkProgressBar(master=self,mode='determinate',
        #                                                  determinate_speed=float(self.set_duration(playlist[i]))/100.0)

        # self.progress_bar.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="nsew")
        # self.progress_bar.start()

    def upvote(self):
        print('add vote')
        self.master.master.database.add_vote(playlist[i], True)
        self.Maj_playlist()


    def downvote(self):
        print('down vote')
        self.master.master.database.add_vote(playlist[i], False)
        self.Maj_playlist()

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
        global playlist, name_song, i

        playlist = self.master.master.database.recup_vote_and_song(self.master.master.room)
        name_song = []
        for fichier in range(len(playlist)):
            name_song.append(playlist[fichier].lstrip('Song/'))
        self.master.master.menu_frame.menu_deroulant.configure(values=name_song)
        self.master.master.music_params.next_title.configure(values=name_song[5])

        self.next_title.configure(text=f"Next title is : {playlist[i + 1].lstrip('../Song/ ')}")
