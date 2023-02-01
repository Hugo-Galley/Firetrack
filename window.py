import customtkinter


class Window(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        if self.master.current_window is not None:
            self.master.current_window.grid_forget()

        # set previous window
        self.previous_window = self.master.current_window

        # set self to current window
        self.master.set_current_window(self)

    def return_to_previous(self):
        self.master.current_window.grid_forget()
        self.master.set_current_window(self.previous_window)