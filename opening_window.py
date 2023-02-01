import customtkinter
import webbrowser
import hashlib

import dev_credit
import join_window
import window
import creation_window
import user_main_windows


class OpeningWindow(window.Window):

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
        creation_window.CreationWindow(master=self.master)

    def join_button_callback(self):
        join_window.JoinWindow(master=self.master)

    @staticmethod
    def open_github():
        webbrowser.open_new('https://github.com/Hugo-Galley/Firetrack')

    def open_credit(self):
        dev_credit.DevCredit(master=self.master)


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
