import customtkinter
import pygame

import window
import database
import room
import user


class MainWindow(window.Window):

    def __init__(self, room_name, room_password, username, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.user = user.User(username)
        self.room = room.Room(name=room_name, password=room_password, creator=self.user)
        self.database = database.DataBase()

        self.user.change_room(self.room)
        self.room.add_user(user)
        self.database.add_room(self.room)
        self.database.add_user(self.user)
