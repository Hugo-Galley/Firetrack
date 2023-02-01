# Importation des modules nécessaires
from tkinter import PhotoImage
import database
import opening_window
import customtkinter
import pygame

# Initialisation de pygame
pygame.mixer.init()

# Configuration du thème
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super(App, self).__init__()

        # Création de la base de données
        self.database = database.DataBase()
        self.database.create_database()

        # Configuration de la fenêtre
        self.geometry("720x480")
        self.title("Firetrack")
        self.minsize(660, 240)

        # Configuration de l'icône de la fenêtre
        self.photo = PhotoImage(file="assets/logo.png")
        self.wm_iconphoto(False, self.photo)

        # Configuration de la grille
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Configuration de la timeline de la fenêtre
        self.current_window = None

        # Affichage de la fenêtre d'ouverture
        self.set_current_window(opening_window.OpeningWindow(master=self))

    def set_current_window(self, elt: object):
        self.current_window = elt
        self.current_window.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    # Lancement de l'application
    app = App()
    app.mainloop()
