import customtkinter
import hashlib
import admin_main_window
import user_main_windows
import window
import database


class CreationWindow(window.Window):

    def __init__(self, *args, **kwargs):
        super(CreationWindow, self).__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.entry_frame = EntryFrame(master=self)
        self.entry_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

        self.button_frame = ButtonFrame(master=self)
        self.button_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    def create_room(self):
        # password = Admin
        if hashlib.sha256(self.entry_frame.room_password_entry.get().encode('utf-8')).hexdigest() and \
                hashlib.sha256(self.entry_frame.username_entry.get().encode('utf-8')).hexdigest() \
                == 'c1c224b03cd9bc7b6a86d77f5dace40191766c485cd55dc48caf9ac873335d6f':
            admin_main_window.AdminMainWindow(master=self.master,
                                              username=self.entry_frame.username_entry.get(),
                                              room_name=self.entry_frame.room_name_entry.get(),
                                              room_password=hashlib.sha256(self.entry_frame.room_password_entry.get().
                                                                           encode('utf-8')).hexdigest()
                                              )

        else:

            user_main_windows.UserMainWindow(master=self.master,
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
