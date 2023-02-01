import customtkinter as ctk
from PIL import Image


class ListUser(ctk.CTkToplevel):

    def __init__(self, database, room, admin=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.database = database
        self.room = room
        self.admin = admin

        self.minsize(720, 480)
        self.geometry("720x480")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.recherche_button_image = ctk.CTkImage(light_image=Image.open("assets/recherche_light_mode.png"),
                                                   dark_image=Image.open("assets/recherche_dark_mode.png"),
                                                   size=(25, 25))

        self.recherche_button = ctk.CTkButton(master=self, image=self.recherche_button_image, text="", height=25,
                                              width=25, fg_color="transparent", command=self.recherche)
        self.recherche_button.grid(row=0, column=0, sticky="nsew")

        self.recherche_bar = ctk.CTkEntry(master=self, placeholder_text="Recherche")
        self.recherche_bar.grid(row=0, column=1, sticky="nsew")

        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=1, sticky="nsew")


    def recherche(self):
        if not self.recherche_bar.get() == "":
            user_list = self.database.recup_users(self.room, username=self.recherche_bar.get())
        else:
            user_list = self.database.recup_users(self.room)

        self.refresh(user_list)

    def refresh(self, user_list):

        for frame in self.scrollable_frame.scrollable_frame.frame_list:
            frame.pack_forget()

        for username, id_user in user_list:
            frame = Frame(master=self.scrollable_frame.scrollable_frame, username=username, id_user=id_user)
            frame.pack(fill="x", anchor="nw", expand=True)
            self.scrollable_frame.scrollable_frame.frame_list.append(frame)


class ScrollableFrame(ctk.CTkFrame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.canvas = ctk.CTkCanvas(self)

        self.scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="nsew")

        self.scrollable_frame = UserFrame(master=self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.bind("<Configure>", self.resize_frame)


        self._id = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set, bg=self._apply_appearance_mode(self._bg_color))
        self.canvas.grid(row=0, column=0, sticky="nsew")

    def resize_frame(self, e):
        self.canvas.itemconfig(self._id, height=e.height-1, width=e.width-2)


class UserFrame(ctk.CTkFrame):

    def __init__(self, lst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.database = self.master.master.master.database

        if lst is None:
            self.user_list = self.database.recup_users(self.master.master.master.room)
        else:
            self.user_list = lst

        self.frame_list = []

        for username, id_user in self.user_list:
            self.frame = Frame(master=self, username=username, id_user=id_user)
            self.frame.pack(fill="x", anchor="nw", expand=True)
            self.frame_list.append(self.frame)

    def kick(self, id_user):
        self.database.kick_user(id_user)
        user_list = self.database.recup_users(self.master.master.master.room)
        self.master.master.master.refresh(user_list)


class Frame(ctk.CTkFrame):

    def __init__(self, username, id_user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(master=self, text=username, font=("Courrier", 20))
        self.label.grid(row=0, column=0, sticky="nsew")

        if self.master.master.master.master.admin:
            self.kick_button = ctk.CTkButton(master=self, text="kick", font=("Courrier", 10), width=20,
                                             command=lambda: self.master.kick(id_user))
            self.kick_button.grid(row=0, column=1, sticky="nsew")
