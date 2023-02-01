from string import ascii_letters, digits
from random import choice
from mutagen.mp3 import MP3
import os
import mysql.connector as mc

CHARACTERS: str = ascii_letters + digits


class DataBase:
    
    def __init__(self):
        self.name: str = "database"
        self.conn = mc.connect(host="mysql-firetrack.alwaysdata.net", user="firetrack",
                               password="ee72742a6c178d50aac432eebcd1eb6ccab947d80db1512ddb9e1165e27d27f5",
                               database="firetrack_bsd")

    def create_database(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Rooms(
                idRoom TEXT UNIQUE,
                name TEXT,
                password TEXT,
                nbr_user INTEGER,
                idCreator TEXT
                
            )
            """
        )
        cursor.execute(
            """    
            CREATE TABLE IF NOT EXISTS Song(
                idSong TEXT UNIQUE,
                song_name TEXT,
                vote INTEGER,
                duration TEXT,
                idRoom TEXT
                
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Users(
                idUser TEXT UNIQUE,
                name TEXT,
                admin BOOL,
                nbr_vote INTEGER,
                idRoom TEXT
            )
        """
        )
        cursor.close()

    def create_id(self):
        id_: str = "".join(choice(CHARACTERS) for _ in range(8))
        existing_id = [*self.get_users_id(), *self.get_rooms_id(), *self.get_songs_id()]
        if id_ not in existing_id:
            return id_
        return self.create_id()

    def set_duration(self,song):
        def audio_duration(duration_):
            mins = duration_ // 60
            duration_ %= 60
            sec = duration_

            return mins, sec

        audio = MP3("Song/" + song + '')
        audio_info = audio.info
        length = int(audio_info.length)
        minutes, seconds = audio_duration(length)
        tuple_ = (minutes, seconds)
        time = ":".join(map(str, tuple_))
        return time

    def recup_song(self, room):

        file_list = os.listdir("Song")
        cursor = self.conn.cursor()

        donnees_liste = []
        playlist = []

        for fichier in range(len(file_list)):
            j = 0
            id_ = self.create_id()
            id_room = room.id
            duration = self.set_duration(file_list[fichier])
            file_list[fichier] = 'Song/' + file_list[fichier]
            playlist.append(file_list[fichier])
            donnees_liste.append((file_list[fichier], j, duration, id_, id_room))

        cursor.execute(""" DELETE FROM Song """)
        cursor.executemany('INSERT INTO Song (title,vote,duration,idSong,idRoom) VALUES (%s, %s, %s, %s, %s)',
                           donnees_liste)
        cursor.close()
        self.conn.commit()
        return playlist

    def add_room(self, room: object):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO Rooms VALUES(%s, %s, %s, %s, %s)
            """, (room.id, room.name, room.password, room.nbr_user, room.creator.id)
        )
        cursor.close()
        self.conn.commit()

    def add_user(self, user: object):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO Users VALUES(%s, %s, %s, %s, %s)
            """, (user.id, user.name, user.admin, user.nbr_vote, user.room.id)
        )
        cursor.close()
        self.conn.commit()

    def get_password(self, id_: str) -> str:
        cursor = self.conn.cursor()
        cursor.execute("SELECT password FROM Rooms WHERE idRoom = %s", (id_,))
        for password in cursor.fetchall():
            cursor.close()
            return password

    def add_vote(self, id_, like, user):
        vote = self.update_user_vote(user)
        if not vote:
            return

        cursor = self.conn.cursor()
        if like:
            command = 'update Song set vote=vote+1 where idSong=%s'
        else:
            command = 'update Song set vote=vote-1 where idSong=%s'
        cursor.execute(command, (id_,))
        cursor.close()
        self.conn.commit()

    def update_user_vote(self, user):
        cur = self.conn.cursor()
        cur.execute("""SELECT nbr_vote FROM Users WHERE idUser = %s""", (user.id,))
        result = cur.fetchone()
        if result[0] == 0:
            vote = False
        else:
            cur.execute("""UPDATE Users set nbr_vote = nbr_vote-1 WHERE idUser = %s""", (user.id,))
            vote = True

        cur.close()
        self.conn.commit()
        return vote

    def get_songs_id(self) -> list[str, ...]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT idSong FROM Song")
        songs_id: list[str, ...] = []
        for elt in cursor.fetchall():
            for id_ in elt:
                songs_id.append(id_)
        cursor.close()
        return songs_id

    def get_users_id(self) -> list[str, ...]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT idUser FROM Users")
        users_id: list[str, ...] = []
        for elt in cursor.fetchall():
            for id_ in elt:
                users_id.append(id_)
        cursor.close()
        return users_id

    def get_rooms_id(self) -> list[str, ...]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT idRoom FROM Rooms")
        rooms_id: list[str, ...] = []
        for elt in cursor.fetchall():
            for id_ in elt:
                rooms_id.append(id_)
        cursor.close()
        return rooms_id

    def get_song_title(self, id_: str) -> str:
        cursor = self.conn.cursor()
        cursor.execute("SELECT song_name FROM Songs WHERE idSongs = ?", (id_,))
        for title in cursor.fetchone():
            cursor.close()
            return title

    def recup_vote_and_song(self, room, title=None, vote=False, id_=False, trie=("vote", "DESC")):
        option, order = trie
        song_playlist_trie = []
        cur = self.conn.cursor()
        if title is None:
            cur.execute(f"""SELECT title,vote,idSong FROM Song WHERE idRoom = %s ORDER BY {option} {order}""",
                        (room.id,))
        else:
            cur.execute(
                f"""SELECT title,vote,idSong FROM Song WHERE title LIKE '{title}%' AND idRoom = %s ORDER BY {option} \
                {order}""", (room.id,)
            )
        result = cur.fetchall()

        if not vote and not id_:
            for i in range(len(result)):
                song_playlist_trie.append(result[i][0])

        elif not vote and id_:
            for i in range(len(result)):
                song_playlist_trie.extend([result[i][0], result[i][2]])

        elif vote and not id_:
            for i in range(len(result)):
                song_playlist_trie.extend(result[i][0:1])

        else:
            cur.close()
            return result

        cur.close()
        return song_playlist_trie

    def recup_users(self, room, username=None):
        cur = self.conn.cursor()
        if username is None:
            cur.execute("""SELECT name, idUser FROM Users WHERE idRoom = %s""", (room.id,))
        else:
            cur.execute(f"""SELECT name, idUser FROM Users WHERE idRoom = %s AND name LIKE '{username}%'""", (room.id,))
        result = cur.fetchall()
        cur.close()
        return result

    def kick_user(self, id_user):
        self.kill_connection(id_user)
        cur = self.conn.cursor()
        cur.execute("""DELETE FROM Users WHERE idUser = %s""", (id_user,))
        cur.close()
        self.conn.commit()

    # Function to kill a specific connection
    def kill_connection(self, user_id):
        cursor = self.conn.cursor()

        # Check if user exist in the Users table
        cursor.execute("SELECT COUNT(*) FROM Users WHERE idUser = %s", (user_id,))
        count = cursor.fetchone()[0]

        if count == 0:
            print("User does not exist.")
        else:
            # Find the connection with the matching user_id
            cursor.execute(
                "SELECT ID FROM information_schema.processlist WHERE USER = (SELECT name FROM Users WHERE idUser = %s)",
                (user_id,))
            result = cursor.fetchone()

            # If a connection is found, kill it
            if result:
                conn_id = result[0]
                cursor.execute("KILL %s", (conn_id,))
                print("Killed connection: ", conn_id)
            else:
                print("No active connection found for this user.")

        cursor.close()

    def delete_song(self, song_id):
        cur = self.conn.cursor()
        cur.execute("""DELETE FROM Song WHERE idSong = %s""", (song_id,))
        cur.close()
        self.conn.commit()

    def add_song(self,song_id):
        cur = self.conn.cursor()
        id = self.create_id()
        donne = (song_id, 0, 'Unknow',id, room.id)
        cur.executemany('INSERT INTO Song (title,vote,duration,idSong,idRoom) VALUES (%s, %s, %s, %s, %s)',
                           )
