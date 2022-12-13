from string import ascii_letters, digits
from random import choice

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
