import customtkinter as ctk
from PIL import Image
import tkinter.filedialog
import urllib, re, os
from pytube import YouTube
import moviepy as mp

import database


class ListSong(ctk.CTkToplevel):

    def __init__(self, database, room, user, admin, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.database = database
        self.room = room
        self.admin = admin
        self.user = user

        self.minsize(720, 480)
        self.geometry("720x480")

        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.main_frame = MainFrame(master=self)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.menu_frame = MenuFrame(master=self)


class MainFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.database = self.master.database
        self.user = self.master.user
        self.room = self.master.room
        self.admin = self.master.admin

        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.menu_state = False

        self.menu_button_image = ctk.CTkImage(light_image=Image.open("assets/menu_light_mode.png"),
                                              dark_image=Image.open("assets/menu_dark_mode.png"),
                                              size=(50, 50))


        self.menu_button = ctk.CTkButton(master=self, image=self.menu_button_image, width=50, height=50,
                                         text="", fg_color="transparent", command=self.open_frame)
        self.menu_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.refresh_button = ctk.CTkButton(master=self, text="Refresh", font=("Courrier", 15),
                                            command=lambda: self.refresh(self.database.recup_vote_and_song(
                                                room=self.room, vote=True, id_=True, trie=self.recherche_frame.trie
                                            )))
        self.refresh_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.recherche_frame = RechercheFrame(master=self)
        self.recherche_frame.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    def refresh(self, song_list):

        for frame in self.scrollable_frame.scrollable_frame.frame_list:
            frame.pack_forget()

        for title, song_vote, song_id in song_list:
            frame = Frame(master=self.scrollable_frame.scrollable_frame, song_name=title, song_id=song_id,
                          song_vote=song_vote)
            frame.pack(fill="x", pady=10, anchor="nw", expand=True)
            self.scrollable_frame.scrollable_frame.frame_list.append(frame)

    def open_frame(self):
        print(f"{self.menu_state=}")
        if not self.menu_state:
            self.master.menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
            self.menu_state = True
            return

        self.master.menu_frame.grid_forget()
        self.menu_state = False
        return


class MenuFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_from_file = ctk.CTkButton(master=self, text="Add from file", font=("courrier", 10),
                                           command=self.get_file)
        self.add_from_file.pack(padx=10, pady=10)

        self.add_from_url = ctk.CTkButton(master=self, text="Add from url", font=("Courrier", 10), command=self.get_url)
        self.add_from_url.pack(padx=10, pady=10)

    def get_file(self):
        fichier = tkinter.filedialog.askopenfilename(title="Ouvrir un fichier",defaultextension=".mp3",filetypes=[("txt fichier",".mp3")])
        title = fichier.split('/')
        title = title[-1]
        self.master.database.DataBase.add_song(title[-1])

    def get_url(self):
        def show_entry_fields():
            music = e2.get()
            print(music)
            master.destroy()

        master = ctk.CTk()
        ctk.CTkLabel(master=self,text="Music").grid(row=1)

        e2 = ctk.CTkEntry(master)

        e2.grid(row=1, column=1)

        ctk.CTkButton(master, text='Add', command=show_entry_fields).grid(row=3,
                                                                      column=1,
                                                                      sticky=ctk.W,
                                                                      pady=4)

        artist = ''
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + show_entry_fields() + artist)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        link = ("https://www.youtube.com/watch?v=" + video_ids[0])
        yt = YouTube(link)
        video = yt.streams.filter(only_audio=True).first()

        # check for destination to save file
        destination = "Song"

        # download the file
        out_file = video.download(output_path=destination)

        my_clip = mp.VideoFileClip(os.path.abspath(out_file))

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'

        my_clip.audio.write_audiofile(new_file)
        my_clip.close()

        os.remove(out_file)



class ScrollableFrame(ctk.CTkFrame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.canvas = ctk.CTkCanvas(self)

        self.scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="nsew")

        self.scrollable_frame = SongFrame(master=self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.bind("<Configure>", self.resize_frame)


        self._id = self.canvas.create_window((0, 1), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set, bg=self._apply_appearance_mode(self._bg_color))
        self.canvas.grid(row=0, column=0, sticky="nsew")

    def resize_frame(self, e):
        self.canvas.itemconfig(self._id, width=e.width-2)


class SongFrame(ctk.CTkFrame):

    def __init__(self, lst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.database = self.master.master.master.database
        self.user = self.master.master.master.user
        self.room = self.master.master.master.room

        if lst is None:
            self.song_list = self.database.recup_vote_and_song(self.master.master.master.room, vote=True, id_=True)
        else:
            self.song_list = lst

        self.frame_list = []

        for song_name, song_vote, song_id in self.song_list:
            self.frame = Frame(master=self, song_name=song_name, song_vote=song_vote, song_id=song_id)
            self.frame.pack(fill="x", pady=10, anchor="nw", expand=True)
            self.frame_list.append(self.frame)

    def delete(self, song_id):
        self.database.delete_song(song_id)
        song_list = self.database.recup_vote_and_song(self.master.master.master.room, vote=True, id_=True)
        self.master.master.master.refresh(song_list)


class Frame(ctk.CTkFrame):

    def __init__(self, song_name, song_vote, song_id, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.song_name = song_name.lstrip("../Song/")
        self.song_vote = song_vote
        self.song_id = song_id

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(master=self, text=self.song_name.rstrip("3pm."), font=("Courrier", 20))
        self.label.grid(row=0, column=0, padx=(20, 10), sticky="nsew")

        self.vote_label = ctk.CTkLabel(master=self, text=f"{self.song_vote} vote", font=("Courrier", 15))
        self.vote_label.grid(row=0, column=1, padx=10, sticky="nsew")

        self.upvote_image_button = ctk.CTkImage(light_image=Image.open('assets/like_light_mode.png'),
                                                dark_image=Image.open('assets/like_dark_mode.png'),
                                                size=(50, 50))

        self.upvote_button = ctk.CTkButton(master=self, image=self.upvote_image_button, width=10, height=10,
                                           fg_color='transparent', text='', command=self.upvote)
        self.upvote_button.grid(row=0, column=3, padx=10, sticky='nsew')

        self.downvote_button_image = ctk.CTkImage(light_image=Image.open('assets/dislike_light_mode.png'),
                                                  dark_image=Image.open('assets/dislike_dark_mode.png'),
                                                  size=(30, 30))

        self.downvote_button = ctk.CTkButton(master=self, image=self.downvote_button_image, width=10,
                                             height=10, fg_color='transparent', text='', command=self.downvote)
        self.downvote_button.grid(row=0, column=4, padx=10, sticky='nsew')

        if self.master.master.master.master.admin:
            self.play_button_image = ctk.CTkImage(light_image=Image.open('assets/play_button_light_mode.png'),
                                                  dark_image=Image.open('assets/play_button_dark_mode.png'))

            self.play_button = ctk.CTkButton(master=self, image=self.play_button_image, width=10, height=10,
                                             fg_color='transparent', text="", command=None)
            self.play_button.grid(row=0, column=2, padx=10, sticky="nsew")
            self.delete_button = ctk.CTkButton(master=self, text="Delete", font=("Courrier", 15), width=20,
                                               command=lambda: self.master.delete(self.song_id))
            self.delete_button.grid(row=0, column=5, padx=(10, 20))

    def upvote(self):
        print('add vote')
        self.master.database.add_vote(self.song_id, True, self.master.user)
        song_list = self.master.database.recup_vote_and_song(self.master.room, vote=True, id_=True,
                                                             trie=self.master.master.master.master.recherche_frame.trie)
        self.master.master.master.master.refresh(song_list)
    def downvote(self):
        print('down vote')
        self.master.database.add_vote(self.song_id, False, self.master.user)
        song_list = self.master.database.recup_vote_and_song(self.master.room, vote=True, id_=True,
                                                             trie=self.master.master.master.master.recherche_frame.trie)
        self.master.master.master.master.refresh(song_list)


class RechercheFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.trie = ("vote", "DESC")

        self.recherche_button_image = ctk.CTkImage(light_image=Image.open("assets/recherche_light_mode.png"),
                                                   dark_image=Image.open("assets/recherche_dark_mode.png"),
                                                   size=(25, 25))

        self.recherche_button = ctk.CTkButton(master=self, image=self.recherche_button_image, text="", height=25,
                                              width=25, fg_color="transparent", command=self.recherche)
        self.recherche_button.pack(side="left", anchor="nw")

        self.recherche_bar = ctk.CTkEntry(master=self, placeholder_text="Recherche")
        self.recherche_bar.pack(side="left", expand=True, fill="x", anchor="n")

        self.trie_option = ctk.CTkOptionMenu(master=self, values=["vote", "title", "duration"],
                                             command=self.trie_option_callback)
        self.trie_option.pack(side="right", anchor="n")

        self.trie_order = ctk.CTkOptionMenu(master=self, values=["DESC", "ASC"], command=self.trie_order_callback)
        self.trie_order.pack(side="right", anchor="ne")

    def recherche(self):
        if not self.recherche_bar.get() == "":
            song_list = self.master.master.database.recup_vote_and_song(self.master.master.room, vote=True, id_=True,
                                                                        title=f"Song/{self.recherche_bar.get()}",
                                                                        trie=self.trie)
        else:
            song_list = self.master.master.database.recup_vote_and_song(self.master.master.room, vote=True, id_=True,
                                                                        trie=self.trie)

        self.master.refresh(song_list)

    def trie_option_callback(self, value):
        option, order = self.trie
        option = value
        self.trie = (option, order)
        song_list = self.master.master.database.recup_vote_and_song(self.master.master.room, vote=True, id_=True,
                                                                    trie=self.trie)
        self.master.refresh(song_list)

    def trie_order_callback(self, value):
        option, order = self.trie
        order = value
        self.trie = (option, order)
        song_list = self.master.master.database.recup_vote_and_song(self.master.master.room, vote=True, id_=True,
                                                                    trie=self.trie)
        self.master.refresh(song_list)
