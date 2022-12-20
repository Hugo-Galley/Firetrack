import os
from string import ascii_letters, digits
from random import choice
from mutagen.mp3 import MP3

import sqlite3


CHARACTERS = ascii_letters + digits


class DataBase:
    
    def __init__(self):
        self.name = "database"
        self.conn = sqlite3.connect(f"{self.name}.db")

    def create_database(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Rooms(
                idRoom TEXT PRIMARY KEY UNIQUE,
                name TEXT,
                password TEXT,
                nbr_user INTEGER,
                idCreator TEXT,
                FOREIGN KEY(idCreator) REFERENCES Users(idUser)
            )
            """
        )
        cursor.execute(
            """    
            CREATE TABLE IF NOT EXISTS Songs(
                idSong TEXT PRIMARY KEY UNIQUE,
                title TEXT,
                vote INTEGER,
                url TEXT,
                duration TEXT,
                idRoom TEXT,
                FOREIGN KEY(idRoom) REFERENCES Rooms(idRoom)
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Users(
                idUser TEXT PRIMARY KEY UNIQUE,
                name TEXT,
                admin BOOL,
                nbr_vote INTEGER,
                idRoom TEXT,
                FOREIGN KEY(idRoom) REFERENCES Rooms(idRoom)
            )
        """
        )
        cursor.close()

    @staticmethod
    def create_id():
        id = "".join(choice(CHARACTERS) for _ in range(8))
        return id

    def recup_song():

        def set_duartion(song):
            def audio_duration(length):
                mins = length // 60
                length %= 60
                seconds = length

                return mins, seconds

            audio = MP3("../Song/" + song + '')
            audio_info = audio.info
            length = int(audio_info.length)
            mins, seconds = audio_duration(length)
            tuple = (mins, seconds)
            time = ":".join(map(str, tuple))
            return time

        file_list = os.listdir("../Song")
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        i = 0
        donnees_liste = []
        playlist = []
        for fichier in range(len(file_list)):
            i += 1
            j = 0
            id = "".join(choice(CHARACTERS) for _ in range(8))
            duration = set_duartion(file_list[fichier])
            file_list[fichier] = '../Song/' + file_list[fichier]
            playlist.append(file_list[fichier])
            donnees_liste.append((file_list[fichier], j, duration, id))

        cursor.execute(""" DELETE FROM 'Song' """)
        cursor.executemany('INSERT INTO Song (title,vote,duration,idSong) VALUES (?, ?, ?, ?)', donnees_liste)
        conn.commit()
        conn.close()
        return playlist


    def add_room(self, room: object):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO Rooms VALUES(?, ?, ?, ?, ?)
            """, (room.id, room.name, room.password, room.nbr_user, room.creator.id)
        )
        cursor.close()
        self.conn.commit()

    def add_user(self, user):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO Users VALUES(?, ?, ?, ?, ?)
            """, (user.id, user.name, user.admin, user.nbr_vote, user.room.id)
        )
        cursor.close()
        self.conn.commit()

    def get_password(self, id: str):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT password FROM Rooms WHERE idRoom = ?", (id,))
        for element in cursor.fetchone():
            password = element
        cursor.close()
        return password
    def addvote(name,like):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        if like:
            command = 'update Song set vote=vote+1 where title=?'
        else:
            command = 'update Song set vote=vote-1 where title=?'
        conn.execute(command, (name,))
        conn.commit()