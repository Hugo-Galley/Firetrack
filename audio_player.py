class Song:

    def __init__(self, database):
        self.database = database
        self.id = self.database.create_id()
        self.title = ...
        self.vote = 0

