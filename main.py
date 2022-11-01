from tkinter import *
import playlist_fonction
import webbrowser
import Class


def startup_window():
    windows = Tk()
    color = '#24A7A7'

    windows.title("Firetrack")
    windows.geometry("480x360")
    windows.minsize(480, 360)
    windows.config(background=color)

    frame = Frame(windows, bg=color)
    a_prpos = Frame(windows, bg=color)
    a_prpos_2 = Frame(windows, bg=color)

    en_tete = Label(frame, text="Bienvenue sur FireTrack", bg=color, fg='white', font=("Courrier", 25))
    en_tete.pack()
    nom = Label(frame, text="Username", bg=color, fg='white', font=("Courier", 13))
    nom.pack()

    entre = Entry(frame)
    entre.pack()

    add_user = Button(frame, text='Add', bg=color, fg='white', font=("Courier", 15),
                      command=lambda: ouverture_process(windows, entre))
    add_user.pack()
    page_github = Button(a_prpos, text="Page Github", bg=color, fg='white', font=("Courier", 14),
                         command=open_github_page)
    page_github.pack()
    nom_dev = Button(a_prpos_2, text="Crédits", bg=color, fg='white', font=('Courier', 14),
                     command=lambda: open_dev(windows))

    nom_dev.pack()

    frame.pack(expand=YES)
    a_prpos.pack(side=LEFT)
    a_prpos_2.pack(side=RIGHT)

    windows.mainloop()


def ouverture_process(windows, entre):
    if entre.get() == "admin":
        admin_windows()

    playlist_fonction.add_user(entre.get())
    windows.destroy()
    playlist_fonction.lecteur_musique()

def open_github_page():
    webbrowser.open_new('https://github.com/Hugo-Galley/Firetrack')


def open_dev(windows):
    windows.destroy()
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
    admin_win = Tk()
    admin_win.geometry("480x360")
    admin_win.minsize(480,360)
    admin_win.config(background='#24A7A7')

    secret =  Frame(admin_win)
    frame = Frame(admin_win)
    Label(secret,text="Ceci est la page admin",bg='#24A7A7',fg='white',font=('Courier',14)).pack(expand=YES)
    Label(frame,text="Mot de passe",bg='#24A7A7',fg='white',font=('Courier',15)).pack(expand=YES)

    saisi_username = Entry(frame)
    saisi_username.pack(expand=YES)
    frame.pack()

    def test():
        if saisi_username.get() == "Motdepasse":
            secret.pack()
        else :
            messagebox = Tk()
            messagebox.geometry("50x50")
            Label(messagebox,text="Mot de passe incorect",wraplength=70,justify=CENTER).pack()
            messagebox.mainloop()


    add_user = Button(admin_win, text='Add', bg='#24A7A7', fg='white', font=("Courier", 15),
                      command=test).pack()
    admin_win.mainloop()


startup_window()
