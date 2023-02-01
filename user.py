class User:

    def __init__(self, database, name):
        self.database = database
        self.name = name
        self.id = f"#{self.database.create_id()}"
        self.admin = False
        self.nbr_vote = 20
        self.room = None

        if self.room is not None:
            self.room_id = self.room.id

    def change_room(self, room: object):
        self.room = room


class Admin(User):

    def __init__(self, database, name):
        super(Admin, self).__init__(database, name)

        self.admin = True
        self.nbr_vote = -1
    def change_room(self, room: object):
        self.room = room
