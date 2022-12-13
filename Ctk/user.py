import database


class User:

    def __init__(self, name):
        self.name = name
        self.id = f"#{database.DataBase.create_id()}"
        self.admin = False
        self.nbr_vote = 20
        self.room = None

    def change_room(self, room: object):
        self.room = room


class Admin(User):

    def __init__(self, name):
        super(Admin, self).__init__(name)

        self.admin = True
        self.nbr_vote = -1
