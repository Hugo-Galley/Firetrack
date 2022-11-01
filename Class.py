class DataBase:

    def __init__(self):
        pass

    def register_in_database(self):
        pass

    def update_database(self):
        pass


class User(DataBase):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.vote_nbr = 50

    def get_name(self):
        return self.name

    def get_vote_nbr(self):
        return self.vote_nbr

    def use_vote(self):
        self.vote_nbr -= 1
        self.update_database()


class Admin(User):

    def __init__(self, name):
        super().__init__(name)
        self.vote_nbr = -1

    def promote(self, user):
        user = Admin(user.name)


class Room(DataBase):

    def __init__(self, name, password=None):
        super().__init__()
        self.name = name
        self.password = password

        if self.password is not None:
            self.is_private = True

        else:
            self.is_private = False

        self.user_list = list()
        self.user_nbr = len(self.user_list)

        self.register_in_database()