import database
import customtkinter


class ErrorWindow(customtkinter.CTkToplevel):
    """En cours de création (phase de test)"""
    """Pour l'instant c bine de la merde"""

    def __init__(self, error_msg, *args, **kwargs):
        super(ErrorWindow, self).__init__(*args, **kwargs)

        self.geometry(f"{120+len(error_msg)*5}x180")
        self.title("ErrorBox")

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.label_frame = LabelFrame(master=self, error_msg=error_msg)
        self.label_frame.grid(row=0, column=0, padx=10, pady=(20, 0), sticky="nsew")

        self.button_frame = ButtonFrame(master=self)
        self.button_frame.grid(row=1, column=0, padx=10, pady=20, sticky="nsew")


class LabelFrame(customtkinter.CTkFrame):

    def __init__(self, error_msg, *args, **kwargs):
        super(LabelFrame, self).__init__(*args, **kwargs)

        self.label = customtkinter.CTkLabel(master=self, text=error_msg, font=("Courrier", 15))
        self.label.pack(expand=True)


class ButtonFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(ButtonFrame, self).__init__(*args, **kwargs)

        self.button = customtkinter.CTkButton(master=self, text="OK", font=("Courrier", 15),
                                              command=self.master.destroy)
        self.button.pack(expand=True)
