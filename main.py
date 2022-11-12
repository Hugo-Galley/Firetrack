import random
from tkinter import *
import playlist_fonction, webbrowser

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
                     command=lambda: open_credits(windows))
    Button(frame, text='Create Room', bg='#24A7A7', fg='white', font=('Courier', 10), command=lambda:create_room(windows=windows)).pack()

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
    admin_win.minsize(480,360)
    admin_win.config(background='#24A7A7')

    secret =  Frame(admin_win,bg='#24A7A7')
    frame = Frame(admin_win,bg='#24A7A7')
    retour = Frame(admin_win,bg='#24A7A7')

    Label(frame, text="Mot de passe", bg='#24A7A7', fg='white', font=('Courier', 15)).pack(expand=YES)
    Label(secret,text="Infos user ",bg='#24A7A7',fg='white',font=('Courier',15)).pack(expand=YES)
    nom_user= Entry(secret)
    nom_user.pack()
    Mdp = Entry(frame)
    Mdp.pack()
    add_button = Button(secret, text='Add', bg='#24A7A7', fg='white', font=('Courier', 15),
                        command=lambda: open_info(nom_user.get() )).pack()
    #reset_button = Button(secret, text='Reset', bg='#24A7A7', fg='white', font=('Courier',15),
                          #command= reset).pack(side=RIGHT)
    frame.pack()

    def test():
        if Mdp.get() == "Motdepasse":
            frame.destroy()
            secret.pack()
        else :
            messagebox = Tk()
            messagebox.geometry("50x50")
            messagebox.maxsize(50,50)
            Label(messagebox,text="Mot de passe incorect",wraplength=70,justify=CENTER).pack()
            messagebox.mainloop()


    add_user = Button(frame, text='Add', bg='#24A7A7', fg='white', font=("Courier", 15),
                      command=test).pack()
    def open_info(nom):
        info = playlist_fonction.recup_info_user(nom)
        if info == []:
            messagebox = Tk()
            messagebox.geometry("80x80")
            messagebox.maxsize(80,80)
            Label(messagebox, text="Aucuns utilisateur n'éxiste à se nom dans la base de données", wraplength=110, justify=CENTER).pack()
            messagebox.mainloop()

        Label(retour,text=info,bg='#24A7A7',fg='white', font=('Courier',15)).pack(expand=YES)
        retour.pack()


    admin_win.mainloop()

def create_room(windows):

    def add_room():
        playlist_fonction.add_room(username=enter_user_room.get(),num=random.randint(0,346))
        win_room.destroy()
        windows.destroy()
        playlist_fonction.lecteur_musique()

    win_room = Tk()
    win_room.geometry("480x360")
    win_room.minsize(480,360)
    win_room.config(background='#24A7A7')


    Label(win_room,text='Crée une Room',bg='#24A7A7', fg='white',font=('Courrier',25)).pack()
    Label(win_room, text='Username', bg='#24A7A7', fg='white', font=('Courrier', 15)).pack()
    enter_user_room = Entry(win_room)
    enter_user_room.pack()

    Button(win_room,text='Add',bg='#24A7A7',fg='white',font=('Courier',13),command=add_room).pack()



    win_room.mainloop()



startup_window()


