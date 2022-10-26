from tkinter import *
import playlist_fonction

def ouverture_process_classe():
     playlist_fonction.add_user(enter_user.get())
     windows.destroy()
     playlist_fonction.lecteur_musqiue()


windows = Tk()

windows.title("Firetrack")
windows.geometry("480x360")
windows.minsize(480,360)
windows.config(background='#24A7A7')

frame = Frame(windows,bg='#24A7A7')

En_tete = Label(frame, text="Bienvenue sur FireTrack",bg='#24A7A7',fg='white',font=("Courrier",25)).pack()
nom = Label(frame, text="Username",bg='#24A7A7',fg='white',font=("Courier",13)).pack()
enter_user = Entry(frame)
enter_user.pack()
classe = Label(frame, text="Classe",bg='#24A7A7',fg='white',font=("Courier",13)).pack()
enter_class = Entry(frame)
enter_class.pack()
add_classe_button = Button(frame,text="Add",font=("Courier",17),bg='#24A7A7',fg='white',command=ouverture_process_classe).pack()

frame.pack()




windows.mainloop()