import random
from tkinter import *
from customtkinter import *

import Class
import playlist_fonction, webbrowser

COLORS = ("#24A7A7", '#24A7A7')
TITLE = "Firetrack"
TEXT_COLOR = 'white'
SIZE = "480x360"
MIN_SIZE = (480, 360)
FONT_NAME = "Courrier"


def open_window():
    # attribut une instance de la class Window à la variable 'obj_window'
    obj_window = Class.Window(TITLE, COLORS, SIZE, MIN_SIZE)

    # attribution l'instance de la fenêtre tkinter à la variable window
    window = obj_window.window

    startup_window(obj_window, window)

    # loop de la fenêtre
    window.mainloop()



def startup_window(obj_window, window):
    obj_window.window_reset()

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
                                       command=lambda: open_credits(obj_window, window))


def ouverture_process(window, entry):
    if entry.get() == "admin":
        return admin_windows()

    playlist_fonction.add_user(entry.get())
    window.destroy()
    playlist_fonction.lecteur_musique()


def open_github_page():
    webbrowser.open_new('https://github.com/Hugo-Galley/Firetrack')


def open_credits(obj_window, window):
    obj_window.window_reset()

    frame_nom = obj_window.create_frame(window, expand=TRUE)
    frame2 = obj_window.create_frame(window, side=LEFT)

    devs_name = obj_window.create_label(frame_nom, "Hugo Galley\n\n Hugo Magnier\n\n Denis Sas\n\n Lusine Matis",
                                        (FONT_NAME, 15))

    back_button = obj_window.create_button(frame2, "Retour", (FONT_NAME, 20),
                                           command=lambda: startup_window(obj_window, window))


def admin_windows():
    def reset():
        retour.destroy()

    admin_win = CTk()
    admin_win.geometry("480x360")
    admin_win.minsize(480, 360)
    admin_win.config(background='#24A7A7')

    secret = CTkFrame(admin_win, bg_color='#24A7A7')
    frame = CTkFrame(admin_win, bg_color='#24A7A7')
    retour = CTkFrame(admin_win, bg_color='#24A7A7')

    CTkLabel(frame, text="Mot de passe", bg_color='#24A7A7', fg_color='#24A7A7', font=('Courier', 15)).pack(expand=YES)
    CTkLabel(secret, text="Infos user ", bg_color='#24A7A7', fg_color='#24A7A7', font=('Courier', 15)).pack(expand=YES)
    nom_user = CTkEntry(secret)
    nom_user.pack()
    Mdp = CTkEntry(frame)
    Mdp.pack()
    add_button = CTkButton(secret, text='Add',text_color='#24A7A7', bg_color='#24A7A7', fg_color='#24A7A7', font=('Courier', 15),
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

    add_user = CTkButton(frame, text='Add', bg_color='#24A7A7', fg_color='white', font=("Courier", 15),
                      command=test).pack()

    def open_info(nom):
        info = playlist_fonction.recup_info_user(nom)
        if info == []:
            messagebox = CTk()
            messagebox.geometry("80x80")
            messagebox.maxsize(80, 80)
            CTkLabel(messagebox, text="Aucuns utilisateur n'éxiste à se nom dans la base de données", wraplength=110,
                  justify=CENTER).pack()
            messagebox.mainloop()

        CTkLabel(retour, text=info, bg_color='#24A7A7', fg_color='#24A7A7', font=('Courier', 15)).pack(expand=YES)
        retour.pack()

    admin_win.mainloop()


def create_room(windows):
    def add_room():
        playlist_fonction.add_room(username=enter_user_room.get(), num=random.randint(0, 346))
        win_room.destroy()
        windows.destroy()
        playlist_fonction.lecteur_musique()

    win_room = CTk()
    win_room.geometry("480x360")
    win_room.minsize(480, 360)
    win_room.config(background='#24A7A7')

    CTkLabel(win_room, text='Crée une Room', bg_color='#24A7A7', fg_color='#24A7A7', font=('Courrier', 25)).pack()
    CTkLabel(win_room, text='Username', bg_color='#24A7A7', fg_color='#24A7A7', font=('Courrier', 15)).pack()
    enter_user_room = CTkEntry(win_room)
    enter_user_room.pack()

    CTkButton(win_room, text='Add', bg_color='#24A7A7', fg_color='#24A7A7', font=('Courier', 13), command=add_room).pack()

    win_room.mainloop()


open_window()
