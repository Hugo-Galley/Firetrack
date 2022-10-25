import tkinter as tk
import sqlite3
import pygame
import lecteur_musique
import playlist_fonction

playlist_fonction


def show_entry_fields():
    playlist_fonction.add_user(e1.get())
    master.quit()
    lecteur_musique.lecteur_musique()
    return 1


master = tk.Tk()
tk.Label(master, text="Nom d'utilisateurs ").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)

tk.Button(master, text='Add', command=show_entry_fields).grid(row=3,
                                                              column=1,
                                                              sticky=tk.W,
                                                              pady=4)


master.mainloop()