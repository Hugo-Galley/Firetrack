from tkinter import *
import playlist_fonction
import webbrowser
import Class


NAME = "Firetrack"
COLOR = ('#24A7A7', "white")
SIZE = "480x360"
MIN_SIZE = (480, 360)
FONT_NAME = "Courrier"


def setup_window():
    window = Class.Window(NAME, COLOR, SIZE, MIN_SIZE)

    set_username_window(window)

    window.window.mainloop()


def set_username_window(window):
    window.window_reset()

    frame = window.create_frame(window.window, expand=TRUE)
    a_prpos = window.create_frame(window.window, side=LEFT)
    a_prpos2 = window.create_frame(window.window, side=RIGHT)

    en_tete = window.create_label(frame, text=f"Bienvenue sur {NAME}", font=(FONT_NAME, 25))
    name = window.create_label(frame, text="Username", font=(FONT_NAME, 13))

    entry = window.create_entry(frame)

    add_user = window.create_button(frame, text='Add', font=(FONT_NAME, 15),
                                    command=lambda: ouverture_process(window, entry))
    page_github = window.create_button(a_prpos, text="Page Github", font=(FONT_NAME, 14),
                                       command=open_github_page)
    nom_dev = window.create_button(a_prpos2, text="Crédits", font=(FONT_NAME, 14),
                                   command=lambda: open_dev(window))


def ouverture_process(window, entre):
    if entre.get() == "admin":
        admin_windows()

    playlist_fonction.add_user(entre.get())
    window.window.destroy()
    playlist_fonction.lecteur_musique()


def open_github_page():
    webbrowser.open_new('https://github.com/Hugo-Galley/Firetrack')


def open_dev(window):
    window.window_reset()

    frame_nom = window.create_frame(window.window, expand=TRUE)
    frame2 = window.create_frame(window.window, side=LEFT)

    noms_des_devs = window.create_label(frame_nom, text="Hugo Galley\n\n Hugo Magnier\n\n Denis Sas\n\n Lusine Matis",
                                        font=(FONT_NAME, 14))

    return_button = window.create_button(frame2, text="Retour", font=(FONT_NAME, 15),
                                         command=lambda: set_username_window(window))


def admin_windows():
    admin_win = Class.Window("Admin", COLOR, SIZE, MIN_SIZE)

    frame = admin_win.create_frame(admin_win.window)

    secret_frame = admin_win.create_frame(admin_win.window)
    secret_frame.pack_forget()

    error_frame = admin_win.create_frame(admin_win.window)
    error_frame.pack_forget()

    label = admin_win.create_label(frame, text="Mot de passe", font=(FONT_NAME, 15))
    secret_label = admin_win.create_label(secret_frame, text="Ceci est la page admin", font=(FONT_NAME, 14))
    error_label = admin_win.create_label(error_frame, text="Mot de passe incorrecte", font=(FONT_NAME, 14))

    username = admin_win.create_entry(frame, expand=TRUE)

    def test():
        if username.get() == "Motdepasse":
            error_frame.pack_forget()
            secret_frame.pack()
        else:
            secret_frame.pack_forget()
            error_frame.pack()

    add_user = admin_win.create_button(admin_win.window, text="Add", font=(FONT_NAME, 15), command=test)

    admin_win.window.mainloop()


if __name__ == "__main__":
    setup_window()