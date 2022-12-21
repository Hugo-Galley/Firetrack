import tkinter.filedialog

fichier = tkinter.filedialog.askopenfilename(title="Ouvrir un fichier", defaultextension=".mp3",
                                   filetypes=[("txt fichier", ".mp3")])
new = fichier.split('/')
new = new[-1]
print(new)
