import tkinter as tk

def choix_artiste():
    def show_entry_fields():
        artist = e1.get()

        master.quit()
        return artist

    master = tk.Tk()
    tk.Label(master, text="Artist ").grid(row=0)


    e1 = tk.Entry(master)


    e1.grid(row=0, column=1)

    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master, text='Show', command=show_entry_fields).grid(row=3,
                                                                   column=1,
                                                                   sticky=tk.W,
                                                                   pady=4)

    master.mainloop()
    return show_entry_fields()
def choix_music():
    def show_entry_fields():
        music = e2.get()
        master.quit()
        return music

    master = tk.Tk()
    tk.Label(master, text="Music ").grid(row=1)

    e2 = tk.Entry(master)


    e2.grid(row=1, column=1)

    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master, text='Show', command=show_entry_fields).grid(row=3,
                                                                   column=1,
                                                                   sticky=tk.W,
                                                                   pady=4)

    master.mainloop()
    return show_entry_fields()
