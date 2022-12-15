from PIL import Image

import customtkinter
import pygame

import window
import database
import room
import user


class AdminMainWindow(window.Window):

    def __init__(self, room_name, room_password, username, *args, **kwargs):
        super(AdminMainWindow, self).__init__(*args, **kwargs)

        self.user = user.User(username)
        self.room = room.Room(name=room_name, password=room_password, creator=self.user)
        self.database = database.DataBase()

        self.user.change_room(self.room)
        self.room.add_user(user)
        self.database.add_room(self.room)
        self.database.add_user(self.user)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.main_frame = MainFrame(master=self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    def open_menu(self):
        pass


class MainFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.song_label = customtkinter.CTkLabel(master=self, text="Current song name", font=("Courrier", 30))
        self.song_label.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        self.menu_button_image = customtkinter.CTkImage(light_image=Image.open("../assets/menu.png"),
                                                        dark_image=Image.open("../assets/menu-modified.png"),
                                                        size=(50, 50))

        self.menu_button = customtkinter.CTkButton(master=self, image=self.menu_button_image, text="", width=50,
                                                   height=50, fg_color="transparent",
                                                   command=self.master.open_menu)
        self.menu_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.music_params = MusicParams(master=self)


class MusicParams(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(MusicParams, self).__init__(*args, **kwargs)

        
