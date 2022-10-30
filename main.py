from tkinter import *
import playlist_fonction
import webbrowser

def ouverture_process():
     playlist_fonction.add_user(entre.get())
     windows.destroy()
     playlist_fonction.lecteur_musqiue()

def open_github_page():
     webbrowser.open_new('https://github.com/Hugo-Galley/Firetrack')


windows = Tk()

windows.title("Firetrack")
windows.geometry("480x360")
windows.minsize(480,360)
windows.config(background='#24A7A7')

frame = Frame(windows,bg='#24A7A7')
a_prpos = Frame(windows,bg='#24A7A7')

En_tete = Label(frame, text="Bienvenue sur FireTrack",bg='#24A7A7',fg='white',font=("Courrier",25)).pack()
nom = Label(frame, text="Username",bg='#24A7A7',fg='white',font=("Courier",13)).pack()

entre = Entry(frame)
entre.pack()

add_user = Button(frame, text='Add', bg='#24A7A7',fg='white',font=("Courier",15),command=ouverture_process).pack()
page_github = Button(a_prpos, text="Page Github",bg='#24A7A7',fg='white',font=("Courrier",14),command=open_github_page).pack()



frame.pack()
a_prpos.pack(side=BOTTOM)



windows.mainloop()