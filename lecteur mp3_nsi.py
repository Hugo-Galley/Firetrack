#PYTHON AUDIO PLAYER!!!


#"""Import Modules"""

import pygame

import tkinter as tkr

import os



#"""Create Window"""

player = tkr.Tk()



#"""Edit Window"""

player.title(" NSI Audio Player")

player.geometry("205x400")





#"""Playlist Register"""

os.chdir("Song")

#print(os.getcwd)

songlist = os.listdir()



#"""Volume Input"""

VolumeLevel = tkr.Scale(player,from_=0.0,to_=1.0,

                        orient = tkr.HORIZONTAL, resolution = 0.1)






#"""Playlist Input"""

playlist = tkr.Listbox(player,highlightcolor="blue",selectmode = tkr.SINGLE)

#print(songlist)

for item in songlist:

    pos = 0

    playlist.insert(pos, item)

    pos = pos + 1



"""Pygame Inits"""

pygame.init()

pygame.mixer.init()



"""Action Event"""

def Play():


    print(var.set(playlist.get(tkr.ACTIVE)))



"""Register Buttons"""

button1 = tkr.Button(player,width=5,height=3, text="PLAY",command=Play)

#"""Create SongName"""

var = tkr.StringVar()

songtitle = tkr.Label(player,textvariable=var)





"""Place Widgets"""

songtitle.pack()

button1.pack(fill="x")

playlist.pack(fill="both", expand="yes")





"""Activate"""
print(var)
player.mainloop()