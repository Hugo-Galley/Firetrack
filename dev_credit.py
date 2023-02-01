import customtkinter
import window


class DevCredit(window.Window):

    def __init__(self, *args, **kwargs):
        super(DevCredit, self).__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.name_frame = NameFrame(master=self)
        self.name_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.previous_button = customtkinter.CTkButton(master=self, text="Retour", font=("Courrier", 20),
                                                       command=self.return_to_previous)
        self.previous_button.grid(row=1, column=0, padx=20, pady=20, sticky="sw")


class NameFrame(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super(NameFrame, self).__init__(*args, **kwargs)

        self.devs_name = customtkinter.CTkLabel(master=self,
                                                text="Hugo Galley\n\n Hugo Magnier\n\n Denis Sas\n\n Lusine Matis",
                                                font=("Courrier", 32))
        self.devs_name.pack(expand=True)