import customtkinter
from tkinter import PhotoImage

import pygame

import database
import opening_window

# configure theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
pygame.mixer.init()


class App(customtkinter.CTk):
    def __init__(self):
        super(App, self).__init__()

        # configure window
        self.geometry("720x480")
        self.title("Firetrack")
        self.minsize(660, 240)

        self.photo = PhotoImage(file="../assets/logo.png")
        self.wm_iconphoto(False, self.photo)

        # configure grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # configure window timeline
        self.current_window = None

        self.set_current_window(opening_window.OpeningWindow(master=self))

    def set_current_window(self, elt: object):
        self.current_window = elt
        self.current_window.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    database1 = database.DataBase()
    database1.create_database()
    app = App()
    app.mainloop()
