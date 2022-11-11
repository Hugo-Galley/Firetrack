from tkinter import *


class Window:

    def __init__(self, name, color, size, minsize):
        self.name = name
        self.size = size
        self.min_width, self.min_height = minsize
        self.bg_color, self.fg_color = color

        self.window = self.creat_window()

        self.widget_list = list()

    def creat_window(self):
        window = Tk()
        window.title(self.name)
        window.geometry(self.size)
        window.minsize(self.min_width, self.min_height)
        window.config(background=self.bg_color)

        return window

    def create_frame(self, master, expand=FALSE, side=None):
        frame = Frame(master, bg=self.bg_color)
        if side is not None:
            frame.pack(expand=expand, side=side)
        else:
            frame.pack(expand=expand)
        self.widget_list.append(frame)

        return frame

    def create_label(self, master, text, font, bg=None, fg=None, expand=FALSE, side=None):
        if bg is None:
            bg = self.bg_color

        if fg is None:
            fg = self.fg_color

        label = Label(master, text=text, font=font, bg=bg, fg=fg)

        if side is not None:
            label.pack(expand=expand, side=side)
        else:
            label.pack(expand=expand)

        self.widget_list.append(label)

        return label

    def create_button(self, master, text, font, bg=None, fg=None, command=None, expand=FALSE, side=None):
        if bg is None:
            bg = self.bg_color

        if fg is None:
            fg = self.fg_color

        button = Button(master, text=text, font=font, bg=bg, fg=fg, command=command)

        if side is not None:
            button.pack(expand=expand, side=side)
        else:
            button.pack(expand=expand)

        self.widget_list.append(button)

        return button

    def create_entry(self, master, expand=FALSE, side=None):
        entry = Entry(master)

        if side is not None:
            entry.pack(expand=expand, side=side)
        else:
            entry.pack(expand=expand)

        self.widget_list.append(entry)

        return entry

    def window_reset(self):
        for widget in self.widget_list:
            widget.pack_forget()

        self.widget_list = list()


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