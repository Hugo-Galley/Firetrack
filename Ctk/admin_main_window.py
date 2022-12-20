from PIL import Image

import customtkinter
import pygame

import window
import database
import room
import user

global i
i = 0


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
        self.appearance_mode_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.vote = ...
        self.add_music = ...

    def appearance_mode_button_callback(self, value):
        customtkinter.set_appearance_mode(value)


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

    def play_button_callback(self):
        self.play_button.grid_forget()
        self.pause_button.grid(row=0, column=1, padx=(10, 0), pady=10, sticky="nsew")

    def back_button_callback(self):
        pass

    def next_button_callback(self):
        pass

    def slider_event(self, value):
        print(f"{value=}")
