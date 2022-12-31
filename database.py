from string import ascii_letters, digits
from random import choice
from mutagen.mp3 import MP3
import operator, sqlite3, os



CHARACTERS: str = ascii_letters + digits


class DataBase:
    
    def __init__(self):
        self.name: str = "database"
        self.conn = sqlite3.connect('Data Base/database.db')

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
                title TEXT,
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
        id: str = "".join(choice(CHARACTERS) for _ in range(8))
        existing_id = [*self.get_users_id(), *self.get_rooms_id(), *self.get_songs_id()]
        if id not in existing_id:
            return id
        return self.create_id()

    def recup_song():

        def set_duartion(song):
            def audio_duration(length):
                mins = length // 60
                length %= 60
                seconds = length

                return mins, seconds

            audio = MP3("Song/" + song + '')
            audio_info = audio.info
            length = int(audio_info.length)
            mins, seconds = audio_duration(length)
            tuple = (mins, seconds)
            time = ":".join(map(str, tuple))
            return time

        file_list = os.listdir("Song")
        conn = sqlite3.connect('Data Base/database.db')
        cursor = conn.cursor()

        i = 0
        donnees_liste = []
        playlist = []
        for fichier in range(len(file_list)):
            i += 1
            j = 0
            id = "".join(choice(CHARACTERS) for _ in range(8))
            id_room = "".join(choice(CHARACTERS) for _ in range(8))
            duration = set_duartion(file_list[fichier])
            file_list[fichier] = 'Song/' + file_list[fichier]
            playlist.append(file_list[fichier])
            donnees_liste.append((file_list[fichier], j, duration, id,id_room))

        cursor.execute(""" DELETE FROM 'Song' """)
        cursor.executemany('INSERT INTO Song (title,vote,duration,idSong,idRoom) VALUES (?, ?, ?, ?, ?)', donnees_liste)
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
        for password in cursor.fetchall():
            cursor.close()
            return password

    def addvote(name, like):
        conn = sqlite3.connect('Data Base/database.db')
        cursor = conn.cursor()
        if like:
            command = 'update Song set vote=vote+1 where title=?'
        else:
            command = 'update Song set vote=vote-1 where title=?'
        conn.execute(command, (name,))
        conn.commit()

    def get_songs_id(self) -> list[str, ...]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT idSong FROM Song")
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

    def recup_vote_and_song():
        song_playlist_trie = []
        conn = sqlite3.connect('Data Base/database.db')
        cur = conn.cursor()
        cur.execute("""SELECT title,vote FROM Song""")
        result = cur.fetchall()
        playlist_triee = sorted(result, key=operator.itemgetter(1), reverse=True)
        for i in range(len(playlist_triee)):
            song_playlist_trie.append(playlist_triee[i][0])
        return song_playlist_trie


