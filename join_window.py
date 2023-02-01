import customtkinter
import hashlib

import user
import window
import database
import user_main_windows


class JoinWindow(window.Window):

    def __init__(self, *args, **kwargs):
        super(JoinWindow, self).__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.entry_frame = EntryFrame(master=self)
        self.entry_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.button_frame = ButtonFrame(master=self)
        self.button_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    def join_room(self):
        user_main_windows.UserMainWindow(master=self.master,
                                         username=self.entry_frame.username_entry.get(),
                                         room_id=self.entry_frame.room_id_entry.get())


        # database1 = database.DataBase()
        # room_id = self.entry_frame.room_id_entry.get()
        # if room_id == "":
        #   return
        # room_password = database1.get_password(room_id)
        # print(f"{room_password=} et {self.entry_frame.room_password_entry.get()=}")
        # if room_password != "":
        #   self.entry_frame.room_password_entry.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        # if room_password == self.entry_frame.room_password_entry.get():
        #   print("hi")


class EntryFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(EntryFrame, self).__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.frame_label = customtkinter.CTkLabel(master=self, text="Join Room", font=("Courrier", 20))
        self.frame_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.username_entry = customtkinter.CTkEntry(master=self, placeholder_text="Enter Username",
                                                     font=("Courrier", 20))
        self.username_entry.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.room_id_entry = customtkinter.CTkEntry(master=self, placeholder_text="Enter Room ID",
                                                    font=("Courrier", 20))
        self.room_id_entry.grid(row=2, column=0, padx=20, pady=(20, 0), sticky="nsew")
        self.room_password_entry = customtkinter.CTkEntry(master=self, font=("Courrier", 20),
                                                          placeholder_text="Enter Room Password")


class ButtonFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(ButtonFrame, self).__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2), weight=1)

        self.create_button = customtkinter.CTkButton(master=self, text="Join", font=("Courrier", 20),
                                                     command=self.master.join_room)
        self.create_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        self.return_button = customtkinter.CTkButton(master=self, text="Retour", font=("Courrier", 15),
                                                     command=self.master.return_to_previous)
        self.return_button.grid(row=1, column=0, padx=20, pady=20, sticky="sw")
