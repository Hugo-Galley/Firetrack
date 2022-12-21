import tkinter.filedialog

fichier = tkinter.filedialog.askopenfilename(title="Ouvrir un fichier", defaultextension=".mp3",
                                   filetypes=[("txt fichier", ".mp3")])
new = fichier.split('/')
new = new[-1]
print(new)


self.slider = customtkinter.CTkSlider(master=self, command=self.slider_event)
        self.slider.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="nsew")