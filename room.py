class Room:

    def __init__(self, database, name: str, password: str, creator: object):
        self.database = database

        self.id = f"#{self.database.create_id()}"

        self.name = name
        self.password = password

        self.list_user = []
        self.nbr_user = len(self.list_user)

        self.creator = creator

    def add_user(self, user: object):
        self.list_user.append(user)

    def get_users(self):
        return self.list_user
