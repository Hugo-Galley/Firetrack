

import pygame

import tkinter as tkr

import os

player = tkr.Tk()
player.title(" NSI Audio Player")
player.geometry("205x400")
songlist = os.listdir("Song")

#"""Playlist Input"""

playlist = tkr.Listbox(player,highlightcolor="blue",selectmode = tkr.SINGLE)
for item in songlist
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1
pygame.init()
pygame.mixer.init()



"""Action Event"""

def Play():

    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))

    var.set(playlist.get(tkr.ACTIVE))

    pygame.mixer.music.play()

    pygame.mixer.music.set_volume(VolumeLevel.get())

    print(pygame.mixer.music.get_volume())

    print(VolumeLevel.get())





def ExitPlayer():

    pygame.mixer.music.stop()




def Pause():

    pygame.mixer.music.pause()




def UnPause():

    pygame.mixer.music.unpause()






"""Register Buttons"""

button1 = tkr.Button(player,width=5,height=3, text="PLAY",command=Play)

button2 = tkr.Button(player, width=5,height=3, text="STOP", command=ExitPlayer)

button3 = tkr.Button(player, width=5,height=3, text="PAUSE", command=Pause)

button4 = tkr.Button(player, width=5,height=3, text="UNPAUSE", command=UnPause)





"""Song Name"""

#"""Create SongName"""

var = tkr.StringVar()

songtitle = tkr.Label(player,textvariable=var)





"""Place Widgets"""

songtitle.pack()

button1.pack(fill="x")

button2.pack(fill="x")

button3.pack(fill="x")

button4.pack(fill="x")

VolumeLevel.pack(fill="x")

playlist.pack(fill="both", expand="yes")





"""Activate"""

player.mainloop()