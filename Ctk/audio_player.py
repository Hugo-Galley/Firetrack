from random import randint


def quick_sort(array):

    n = len(array)

    if n < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, n - 1)]

    for item in array:

        if item.get_nbr_vote > pivot.get_nbr_vote:
            high.append(item)
        elif item.get_nbr_vote == pivot.get_nbr_vote:
            same.append(item)
        else:
            low.append(item)

    return quick_sort(low) + same + quick_sort(high)


class Song:

    def __init__(self, database, title: str, vote: int, path: str, duration: str, id_room: str):
        self.database = database
        self.id_song: str = self.database.create_id()
        self.title: str = title
        self.nbr_vote: int = vote
        self.path: str = path
        self.duration: str = duration
        self.id_room: str = id_room

    def get_nbr_vote(self):
        return self.nbr_vote

    def get_all_attributes(self) -> tuple:
        return self.id_song, self.title, self.nbr_vote, self.duration, self.id_room

    def update_vote(self):
        pass


class Playlist:

    def __init__(self):
        self.song_list: list = []

    def add_song(self, song: Song):
        self.song_list.append(song)

    def sort(self):
        quick_sort(self.song_list)
