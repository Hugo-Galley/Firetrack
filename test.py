import pygame
import tkinter as tkr
import os

player = tkr.Tk()
player.title(" NSI Audio Player")
player.geometry("205x400")
os.chdir("Song")

songlist = os.listdir()
playlist = tkr.Listbox(player,highlightcolor="blue",selectmode = tkr.SINGLE)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1
var = tkr.StringVar()
songtitle = tkr.Label(player,textvariable=var)
songtitle.pack()
playlist.pack(fill="both", expand="yes")
print(songtitle)
player.mainloop()
