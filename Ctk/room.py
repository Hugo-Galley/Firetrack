import database


class Room:

    def __init__(self, name: str, password: str, creator: object):

        self.id = f"#{database.DataBase.create_id()}"

        self.name = name
        self.password = password

        self.list_user = []
        self.nbr_user = len(self.list_user)

        self.creator = creator

    def add_user(self, user: object):
        self.list_user.append(user)
