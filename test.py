

        self.menu_deroulant = customtkinter.CTkComboBox(master=self, values=name_song,
                                                        command=self.choix_musique_button)
        self.menu_deroulant.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        self.info_supplementaire_image = customtkinter.CTkImage(
            light_image=Image.open('assets/light_info_icon (1).png'),
            dark_image=Image.open('assets/dark_info_icon (1).png'),
            size=(30, 30)
        )
        self.info_supplementaire = customtkinter.CTkButton(master=self, image=self.info_supplementaire_image, width=10,
                                                           height=10, fg_color='transparent', text='',
                                                           command=self.info)

        self.info_supplementaire.grid(row=5, column=0, padx=10, pady=10, sticky='nsew')




@staticmethod
def info():
    print('Ca marche batard')
