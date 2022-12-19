
import customtkinter


class TestWindow(customtkinter.CTk):

    customtkinter.set_default_color_theme("dark-blue")
    customtkinter.set_appearance_mode("dark")

    def __init__(self, *args, **kwargs):
        super(TestWindow, self).__init__(*args, **kwargs)

        self.geometry("720x480")
        self.title("TestWindow")

        self.current_window = None

        self.error = error_window.ErrorWindow("Bonjour")
        self.error.mainloop()

    def set_current_window(self, elt: object):
        self.current_window = elt
        self.current_window.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    """user1 = user.User("user")
    room1 = room.Room("room", "", user1)
    print(f"{room1.id=}")
    database1 = database.DataBase()
    database1.create_database()
    database1.add_room_to_database(room1)"""
    test = TestWindow()
    test.mainloop()