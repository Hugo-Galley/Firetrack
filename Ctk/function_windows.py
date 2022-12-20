from PIL import Image
import customtkinter
import pygame
import database
import fonction
import webbrowser
from mutagen.mp3 import MP3

import join_window

global i
i = 0

class Window(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        if self.master.current_window is not None:
            self.master.current_window.grid_forget()

        # set previous window
        self.previous_window = self.master.current_window

        # set self to current window
        self.master.set_current_window(self)

    def return_to_previous(self):
        self.master.current_window.grid_forget()
        self.master.set_current_window(self.previous_window)


class DevCredit(Window):

    def __init__(self, *args, **kwargs):
        super(DevCredit, self).__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.name_frame = NameFrame(master=self)
        self.name_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.previous_button = customtkinter.CTkButton(master=self, text="Retour", font=("Courrier", 20),
                                                       command=self.return_to_previous)
        self.previous_button.grid(row=1, column=0, padx=20, pady=20, sticky="sw")


class NameFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(NameFrame, self).__init__(*args, **kwargs)

        self.devs_name = customtkinter.CTkLabel(master=self,
                                                text="Hugo Galley\n\n Hugo Magnier\n\n Denis Sas\n\n Lusine Matis",
                                                font=("Courrier", 32))
        self.devs_name.pack(expand=True)



class AdminMainWindow(Window):

    def __init__(self, room_name, room_password, username, *args, **kwargs):
        super(AdminMainWindow, self).__init__(*args, **kwargs)

        self.user = fonction.User(username)
        self.room = fonction.Room(name=room_name, password=room_password, creator=self.user)
        self.database = database.DataBase()

        self.user.change_room(self.room)
        self.room.add_user(fonction)
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

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.song_label = customtkinter.CTkLabel(master=self, text=playlist[i].lstrip('../Song/ '), font=("Courrier", 30))
        self.song_label.grid(row=0, rowspan=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.menu_button_image = customtkinter.CTkImage(light_image=Image.open("../assets/menu_dark_mode.png"),
                                                        dark_image=Image.open("../assets/menu_light_mode.png"),
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

        self.grid_columnconfigure(0, weight=1)

        self.appearance_mode_button = customtkinter.CTkOptionMenu(master=self, values=["dark", "light", "system"],
                                                                  command=self.appearance_mode_button_callback)
        self.appearance_mode_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew",)

        self.name_slider = customtkinter.CTkLabel(master=self, text='Volume',text_color='white',font=("",16))
        self.name_slider.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.slider = customtkinter.CTkSlider(master=self, command= self.slider_event_volume,progress_color='red')
        self.slider.grid(row=2, column=0, padx=10, pady=20, sticky="nsew")

        self.upvote_image_button = customtkinter.CTkImage(light_image=Image.open('../assets/like_light_mode.png'),
                                                          dark_image=Image.open('../assets/like_dark_mode.png'),
                                                          size= (50,50))

        self.upvote_button = customtkinter.CTkButton(master=self, image=self.upvote_image_button,width=10,height=10,
                                                     fg_color='transparent',text='',command=self.upvote)
        self.upvote_button.grid(row=3,column=0,padx=10, pady=20, sticky='nsew')

        self.disvote_button_image = customtkinter.CTkImage(light_image=Image.open('../assets/dislike_light_mode.png'),
                                                           dark_image=Image.open('../assets/dislike_dark_mode.png'),
                                                           size=(30,30))
        self.disvote_button = customtkinter.CTkButton(master=self, image=self.disvote_button_image, width=10, height=10,
                                                      fg_color='transparent',text='',command=self.disvote)
        self.disvote_button.grid(row=4,column=0,padx=10, pady=20, sticky='nsew')

    def appearance_mode_button_callback(self, value):
        customtkinter.set_appearance_mode(value)

    def slider_event_volume(self, value):
        pygame.mixer.music.set_volume(value)

    def upvote(self):
        print(playlist[i])
        database.DataBase.addvote(True,playlist[i])

    def disvote(self):
        print(playlist[i])
        database.DataBase.addvote(False,playlist[i])

class MusicParams(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(MusicParams, self).__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.back_button_image = customtkinter.CTkImage(
            light_image=Image.open("../assets/precedent_button_light_mode.png"),
            dark_image=Image.open("../assets/precedent_button_dark_mode.png")
        )
        self.next_button_image = customtkinter.CTkImage(light_image=Image.open("../assets/next_button_light_mode.png"),
                                                        dark_image=Image.open("../assets/next_button_dark_mode.png"))
        self.pause_button_image = customtkinter.CTkImage(light_image=Image.open("../assets/pause_buton_light_mode.png"),
                                                         dark_image=Image.open("../assets/pause_buton_dark_mode.png"))
        self.play_button_image = customtkinter.CTkImage(light_image=Image.open("../assets/play_button_light_mode.png"),
                                                        dark_image=Image.open("../assets/play_button_dark_mode.png"))

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
        pygame.mixer.music.load(playlist[i])
        pygame.mixer.music.play()
        pygame.mixer.music.queue(playlist[i - 1])
        self.song_label = customtkinter.CTkLabel(master=self.master, text=playlist[i].lstrip('../Song/'), font=("Courrier", 30))
        self.song_label.grid(row=0, rowspan=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    def next_button_callback(self):
        global i
        if i < len(playlist) - 2:
            i+=1
        else:
            i = 0
        pygame.mixer.music.load(playlist[i])
        pygame.mixer.music.play()
        pygame.mixer.music.queue(playlist[i + 1])
        self.song_label = customtkinter.CTkLabel(master=self.master, text=playlist[i].lstrip('../Song/'), font=("Courrier", 30))
        self.song_label.grid(row=0, rowspan=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    def slider_event(self, value):
        pygame.mixer.music.set_volume(value)

    def set_duartion(song):
        def audio_duration(length):
            mins = length // 60
            length %= 60
            seconds = length

            return mins, seconds

        audio = MP3("../Song/" + song + '')
        audio_info = audio.info
        length = int(audio_info.length)
        mins, seconds = audio_duration(length)
        tuple = (mins, seconds)
        time = ".".join(map(str, tuple))
        return time




class OpeningWindow(Window):

    def __init__(self, *args, **kwargs):
        super(OpeningWindow, self).__init__(*args, **kwargs)

        # configure 2x2 grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button_frame = ButtonFrame(master=self)
        self.button_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.dev_frame = DevFrame(master=self)
        self.dev_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    def create_button_callback(self):
        CreationWindow(master=self.master)

    def join_button_callback(self):
        join_window.JoinWindow(master=self.master)

    @staticmethod
    def open_github():
        webbrowser.open_new('https://github.com/Hugo-Galley/Firetrack')

    def open_credit(self):
        DevCredit(master=self.master)


class ButtonFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(ButtonFrame, self).__init__(*args, **kwargs)

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # create a label
        self.name_label = customtkinter.CTkLabel(master=self, text="Firetrack", font=("Courrier", 40))
        self.name_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        # create buttons
        self.create_room_button = customtkinter.CTkButton(master=self, text="Create Room", font=("Courrier", 20),
                                                          command=self.master.create_button_callback)
        self.create_room_button.grid(row=1, column=0, padx=(20, 10), pady=20)
        self.join_room_button = customtkinter.CTkButton(master=self, text="Join Room", font=("Courrier", 20),
                                                        command=self.master.join_button_callback)
        self.join_room_button.grid(row=1, column=1, padx=(10, 20), pady=20)


class DevFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(DevFrame, self).__init__(*args, **kwargs)

        self.github_button = customtkinter.CTkButton(master=self, text="Github", font=("Courrier", 20),
                                                     command=self.master.open_github)
        self.github_button.pack(padx=20, pady=20, side=customtkinter.LEFT)
        self.dev_credit_button = customtkinter.CTkButton(master=self, text="Credit", font=("Courrier", 20),
                                                         command=self.master.open_credit)
        self.dev_credit_button.pack(padx=20, pady=20, side=customtkinter.RIGHT)


playlist = []
class CreationWindow(Window):

    def __init__(self, *args, **kwargs):
        super(CreationWindow, self).__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.entry_frame = EntryFrame(master=self)
        self.entry_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

        self.button_frame = ButtonFrame(master=self)
        self.button_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    def create_room(self):
        for i in database.DataBase.recup_song():
            playlist.append(i)
        pygame.mixer.music.load(playlist[0])
        pygame.mixer.music.play()
        AdminMainWindow(master=self.master,
                                    username=self.entry_frame.username_entry.get(),
                                    room_name=self.entry_frame.room_name_entry.get(),
                                    room_password=self.entry_frame.room_password_entry.get())


class EntryFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(EntryFrame, self).__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.frame_label = customtkinter.CTkLabel(master=self, text="Room Creation", font=("Courrier", 20))
        self.frame_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.username_entry = customtkinter.CTkEntry(master=self, placeholder_text="Enter Username",
                                                     font=("Courrier", 20))
        self.username_entry.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.room_name_entry = customtkinter.CTkEntry(master=self, placeholder_text="Enter Room Name",
                                                      font=("Courrier", 20))
        self.room_name_entry.grid(row=2, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.room_password_entry = customtkinter.CTkEntry(master=self, font=("Courrier", 20),
                                                          placeholder_text="Enter Room Password For Private Room")
        self.room_password_entry.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")


class ButtonFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(ButtonFrame, self).__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2), weight=1)

        self.create_button = customtkinter.CTkButton(master=self, text="Create", font=("Courrier", 20),
                                                     command=self.master.create_room)
        self.create_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        self.return_button = customtkinter.CTkButton(master=self, text="Retour", font=("Courrier", 15),
                                                     command=self.master.return_to_previous)
        self.return_button.grid(row=1, column=0, padx=20, pady=20, sticky="sw")
