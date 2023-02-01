from tkinter import *
from customtkinter import *
def create_room():

    win_room = CTk()
    win_room.geometry("480x360")
    win_room.minsize(480, 360)
    win_room.config(background='#24A7A7')

    CTkLabel(win_room, text='Crée une Room', bg_color='#24A7A7', fg_color='#24A7A7', font=('Courrier', 25)).pack()
    CTkLabel(win_room, text='Username', bg_color='#24A7A7', fg_color='#24A7A7', font=('Courrier', 15)).pack()
    enter_user_room = CTkEntry(win_room)
    enter_user_room.pack()

    CTkButton(win_room, text='Add', bg_color='#24A7A7', fg_color='#24A7A7', font=('Courier', 13),).pack()

    win_room.mainloop()
create_room()