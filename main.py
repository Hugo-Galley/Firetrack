from tkinter import *
import playlist_fonction
import webbrowser

def ouverture_process():
     playlist_fonction.add_user(entre.get())
     windows.destroy()
     playlist_fonction.lecteur_musqiue()

def open_github_page():
     webbrowser.open_new('https://github.com/Hugo-Galley/Firetrack')

def open_dev():
     windows.destroy()
     dev_win = Tk()
     dev_win.geometry('480x360')
     dev_win.minsize(480, 360)
     dev_win.config(background='#24A7A7')

     frame_nom = Frame(dev_win)

     noms_des_devs = Label(frame_nom, text="Hugo Galley\n\n Hugo Magnier\n\n Denis Sas\n\n Lusine Matis",
                           bg='#24A7A7', fg='white', font=('Courier', 14)).pack()
     frame_nom.pack(expand=YES)
     dev_win.mainloop()


windows = Tk()

windows.title("Firetrack")
windows.geometry("480x360")
windows.minsize(480,360)
windows.config(background='#24A7A7')

frame = Frame(windows,bg='#24A7A7')
a_prpos = Frame(windows,bg='#24A7A7')
a_prpos_2 = Frame(windows,bg='#24A7A7')

En_tete = Label(frame, text="Bienvenue sur FireTrack",bg='#24A7A7',fg='white',font=("Courrier",25)).pack()
nom = Label(frame, text="Username",bg='#24A7A7',fg='white',font=("Courier",13)).pack()

entre = Entry(frame)
entre.pack()

add_user = Button(frame, text='Add', bg='#24A7A7',fg='white',font=("Courier",15),command=ouverture_process).pack()
page_github = Button(a_prpos, text="Page Github",bg='#24A7A7',fg='white',font=("Courier",14),command=open_github_page).pack()
nom_dev = Button(a_prpos_2, text="Crédits", bg='#24A7A7',fg='white',font=('Courier',14),command=open_dev).pack()


frame.pack(expand=YES)
a_prpos.pack(side= LEFT)
a_prpos_2.pack(side=RIGHT)

windows.mainloop()
