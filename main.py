import random
from tkinter import *

import Class
import playlist_fonction, webbrowser

COLORS = ("#24A7A7", "white")
TITLE = "Firetrack"
SIZE = "480x360"
MIN_SIZE = (480, 360)
FONT_NAME = "Courrier"


def startup_window():
    # attribut une instance de la class Window à la variable 'obj_window'
    obj_window = Class.Window(TITLE, COLORS, SIZE, MIN_SIZE)

    # attribution l'instance de la fenêtre tkinter à la variable window
    window = obj_window.window

    # creation des frames
    frame = obj_window.create_frame(window, expand=TRUE)
    a_prpos = obj_window.create_frame(window, side=LEFT)
    a_prpos_2 = obj_window.create_frame(window, side=RIGHT)

    # creation des labels
    en_tete = obj_window.create_label(frame, f"Bienvenue sur {TITLE}", (FONT_NAME, 25))
    name = obj_window.create_label(frame, "Username", (FONT_NAME, 13))

    # creation du champ d'entré
    entry = obj_window.create_entry(frame)

    # creation des boutons
    add_user = obj_window.create_button(frame, "Add", (FONT_NAME, 15),
                                        command=lambda: ouverture_process(window, entry))

    room = obj_window.create_button(frame, "Create Room", (FONT_NAME, 10),
                                    command=lambda: create_room(window))

    page_github = obj_window.create_button(a_prpos, "Page Github", (FONT_NAME, 14),
                                           command=open_github_page)

    nom_dev = obj_window.create_button(a_prpos_2, "Crédits", (FONT_NAME, 14),
                                       command=lambda: open_credits(window))

    # loop de la fenêtre
    window.mainloop()


def ouverture_process(windows, entre):
    if entre.get() == "admin":
        admin_windows()

    playlist_fonction.add_user(entre.get())
    windows.destroy()
    playlist_fonction.lecteur_musique()


def open_github_page():
    webbrowser.open_new('https://github.com/Hugo-Galley/Firetrack')


def open_credits(windows):
    dev_win = Tk()
    dev_win.geometry('480x360')
    dev_win.minsize(480, 360)
    dev_win.config(background='#24A7A7')

    frame_nom = Frame(dev_win)

    noms_des_devs = Label(frame_nom, text="Hugo Galley\n\n Hugo Magnier\n\n Denis Sas\n\n Lusine Matis",
                          bg='#24A7A7', fg='white', font=('Courier', 14))
    noms_des_devs.pack()
    frame_nom.pack(expand=YES)
    dev_win.mainloop()


def admin_windows():
    def reset():
        retour.destroy()

    admin_win = Tk()
    admin_win.geometry("480x360")
    admin_win.minsize(480, 360)
    admin_win.config(background='#24A7A7')

    secret = Frame(admin_win, bg='#24A7A7')
    frame = Frame(admin_win, bg='#24A7A7')
    retour = Frame(admin_win, bg='#24A7A7')

    Label(frame, text="Mot de passe", bg='#24A7A7', fg='white', font=('Courier', 15)).pack(expand=YES)
    Label(secret, text="Infos user ", bg='#24A7A7', fg='white', font=('Courier', 15)).pack(expand=YES)
    nom_user = Entry(secret)
    nom_user.pack()
    Mdp = Entry(frame)
    Mdp.pack()
    add_button = Button(secret, text='Add', bg='#24A7A7', fg='white', font=('Courier', 15),
                        command=lambda: open_info(nom_user.get())).pack()
    # reset_button = Button(secret, text='Reset', bg='#24A7A7', fg='white', font=('Courier',15),
    # command= reset).pack(side=RIGHT)
    frame.pack()

    def test():
        if Mdp.get() == "Motdepasse":
            frame.destroy()
            secret.pack()
        else:
            messagebox = Tk()
            messagebox.geometry("50x50")
            messagebox.maxsize(50, 50)
            Label(messagebox, text="Mot de passe incorect", wraplength=70, justify=CENTER).pack()
            messagebox.mainloop()

    add_user = Button(frame, text='Add', bg='#24A7A7', fg='white', font=("Courier", 15),
                      command=test).pack()

    def open_info(nom):
        info = playlist_fonction.recup_info_user(nom)
        if info == []:
            messagebox = Tk()
            messagebox.geometry("80x80")
            messagebox.maxsize(80, 80)
            Label(messagebox, text="Aucuns utilisateur n'éxiste à se nom dans la base de données", wraplength=110,
                  justify=CENTER).pack()
            messagebox.mainloop()

        Label(retour, text=info, bg='#24A7A7', fg='white', font=('Courier', 15)).pack(expand=YES)
        retour.pack()

    admin_win.mainloop()


def create_room(windows):
    def add_room():
        playlist_fonction.add_room(username=enter_user_room.get(), num=random.randint(0, 346))
        win_room.destroy()
        windows.destroy()
        playlist_fonction.lecteur_musique()

    win_room = Tk()
    win_room.geometry("480x360")
    win_room.minsize(480, 360)
    win_room.config(background='#24A7A7')

    Label(win_room, text='Crée une Room', bg='#24A7A7', fg='white', font=('Courrier', 25)).pack()
    Label(win_room, text='Username', bg='#24A7A7', fg='white', font=('Courrier', 15)).pack()
    enter_user_room = Entry(win_room)
    enter_user_room.pack()

    Button(win_room, text='Add', bg='#24A7A7', fg='white', font=('Courier', 13), command=add_room).pack()

    win_room.mainloop()


startup_window()
