from string import ascii_letters, digits
from random import choice

import sqlite3


CHARACTERS: str = ascii_letters + digits


class DataBase:
    
    def __init__(self):
        self.name: str = "database"
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

    def create_id(self):
        id: str = "".join(choice(CHARACTERS) for _ in range(8))
        existing_id = [*self.get_users_id(), *self.get_rooms_id(), *self.get_songs_id()]
        if id not in existing_id:
            return id
        return self.create_id()

    def add_room(self, room: object):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO Rooms VALUES(?, ?, ?, ?, ?)
            """, (room.id, room.name, room.password, room.nbr_user, room.creator.id)
        )
        cursor.close()
        self.conn.commit()

    def add_user(self, user: object):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO Users VALUES(?, ?, ?, ?, ?)
            """, (user.id, user.name, user.admin, user.nbr_vote, user.room.id)
        )
        cursor.close()
        self.conn.commit()

    def get_password(self, id: str) -> str:
        cursor = self.conn.cursor()
        cursor.execute("SELECT password FROM Rooms WHERE idRoom = ?", (id,))
        for password in cursor.fetchone():
            cursor.close()
            return password

    def get_songs_id(self) -> list[str, ...]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT idSong FROM Songs")
        songs_id: list[str, ...] = []
        for elt in cursor.fetchall():
            for id in elt:
                songs_id.append(id)
        cursor.close()
        return songs_id

    def get_users_id(self) -> list[str, ...]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT idUser FROM Users")
        users_id: list[str, ...] = []
        for elt in cursor.fetchall():
            for id in elt:
                users_id.append(id)
        cursor.close()
        return users_id

    def get_rooms_id(self) -> list[str, ...]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT idRoom FROM Rooms")
        rooms_id: list[str, ...] = []
        for elt in cursor.fetchall():
            for id in elt:
                rooms_id.append(id)
        cursor.close()
        return rooms_id

    def get_song_title(self, id: str) -> str:
        cursor = self.conn.cursor()
        cursor.execute("SELECT title FROM Songs WHERE idSongs = ?", (id,))
        for title in cursor.fetchone():
            cursor.close()
            return title
