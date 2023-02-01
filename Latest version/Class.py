from tkinter import *
import customtkinter as tkc


class Playlist:

    playlist = list()
    is_empty = True
    cursor = 0
    max_cursor = 0

    # ajoute une ou plusieurs musiques à la playliste
    def add_song(self, song):
        # regarde si c'est une liste de musique ou juste une à ajouter
        # ajoute la ou les musiques avec la méthode approprié
        if song is list:
            self.playlist.extend(song)
        else:
            self.playlist.append(song)

        # réadapte la position max
        self.max_cursor = len(self.playlist)
        # change le statu de la playliste à non-vide
        self.is_empty = False

    # supprime une ou plusieurs musiques de la playliste
    def delete_song(self, song):
        # vérifi si la playliste est vide
        if self.is_empty:
            return print("Oppération impossible, votre playliste est vide")

        # regarde si c'est une liste de musique ou juste une à supprimer
        # supprime la ou les musiques avec la méthode approprié
        if song is list:
            for element in song:
                self.playlist.remove(element)
        else:
            self.playlist.remove(song)

        # réadapte la position max
        self.max_cursor = len(self.playlist)

        # vérifi si la playliste est devenu vide après la supprétion des element
        if len(self.playlist) == 0:
            self.is_empty = True

    # renvoie les musiques contenues dans la playliste
    def get_song(self):
        return self.playlist

    # réinitialise la playliste et la position max
    def reset_playlist(self):
        self.playlist = list()
        self.max_cursor = 0

    # renvoie la musique actuelle
    def current_song(self):
        return self.playlist[self.cursor]

    # passe à la musique suivante
    def next(self):
        if self.cursor < self.max_cursor:
            self.cursor += 1
        else:
            self.cursor = 0

    # reviens à la musique précédente
    def previous(self):
        if self.cursor > 0:
            self.cursor -= 1
        else:
            self.cursor = self.max_cursor

    # change la musique et adapte le cursor à la position de la musique
    def change_song(self, song):
        if song in self.playlist:
            self.cursor = self.playlist.index(song)
        else:
            print("Cette chanson n'est pas dans la playliste")


# class Window pour simplifier la creation de fenêtre tkinter
class Window:

    def __init__(self, name, color, size, minsize):
        # attribution de tous les paramètres de la fenêtre
        self.name = name
        self.size = size
        self.min_width, self.min_height = minsize
        self.bg_color, self.fg_color = color

        # creation de l'instance de la fenêtre tkinter
        self.window = self.creat_window()

        # liste de tous les widgets enfants de la fenêtre
        self.widget_list = list()

    def creat_window(self):
        # crée l'instance de la fenêtre tkinter avec les paramètres de la class Window
        window = tkc.CTk()
        window.title(self.name)
        window.geometry(self.size)
        window.minsize(self.min_width, self.min_height)
        window.config(background=self.bg_color)

        return window

    def create_frame(self, master, expand=FALSE, side=None):
        frame = tkc.CTkFrame(master, bg_color=self.bg_color)

        if side is not None:
            frame.pack(expand=expand, side=side)
        else:
            frame.pack(expand=expand)

        # ajoute la frame créée à la liste de widgets
        self.widget_list.append(frame)

        return frame

    def create_label(self, master, text, font, bg=None, fg=None, expand=FALSE, side=None):
        if bg is None:
            bg = self.bg_color

        if fg is None:
            fg = self.fg_color

        label = tkc.CTkLabel(master, text=text, font=font, bg_color=bg, fg_color=fg)

        if side is not None:
            label.pack(expand=expand, side=side)
        else:
            label.pack(expand=expand)

        # ajoute le label créée à la liste de widgets
        self.widget_list.append(label)

        return label

    def create_button(self, master, text, font, bg=None, fg=None, command=None, expand=FALSE, side=None):
        if bg is None:
            bg = self.bg_color

        if fg is None:
            fg = self.fg_color

        button = tkc.CTkButton(master, text=text, font=font, bg_color=bg, fg_color=fg, command=command)

        if side is not None:
            button.pack(expand=expand, side=side)
        else:
            button.pack(expand=expand)

        # ajoute le bouton créée à la liste de widgets
        self.widget_list.append(button)

        return button

    def create_entry(self, master, expand=FALSE, side=None):
        entry = tkc.CTkEntry(master)

        if side is not None:
            entry.pack(expand=expand, side=side)
        else:
            entry.pack(expand=expand)

        # ajoute le champ d'entré créée à la liste de widgets
        self.widget_list.append(entry)

        return entry

    def window_reset(self):
        # reset les widgets présent dans la fenêtre
        for widget in self.widget_list:
            widget.pack_forget()

        # reset la liste des widgets enfants de la fenêtre
        self.widget_list = list()


class DataBase:

    def __init__(self):
        pass

    def register_in_database(self):
        pass

    def update_database(self):
        pass


class User(DataBase):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.vote_nbr = 50

    def get_name(self):
        return self.name

    def get_vote_nbr(self):
        return self.vote_nbr

    def use_vote(self):
        self.vote_nbr -= 1
        self.update_database()


class Admin(User):

    def __init__(self, name):
        super().__init__(name)
        self.vote_nbr = -1

    def promote(self, user):
        user = Admin(user.name)


class Room(DataBase):

    def __init__(self, name, password=None):
        super().__init__()
        self.name = name
        self.password = password

        if self.password is not None:
            self.is_private = True

        else:
            self.is_private = False

        self.user_list = list()
        self.user_nbr = len(self.user_list)

        self.register_in_database()