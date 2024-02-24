#importing libraries 
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os


#creating the root window 
root=Tk()
root.geometry("485x700+290+10")
root.title("Music Player")
root.configure(background="grey")
root.resizable(False, False)
#initialize mixer 
mixer.init()

#add many songs to the playlist
def AddMusic():
    path= filedialog.askdirectory()
    if path:
        os.chdir(path)
    songs=os.listdir(path)

    for song in songs:
      if song.endswith(".mp3"):
            Playlist.insert(END, song)

#to play the songs
def PlayMusic():
    Music_Name=Playlist.get(ACTIVE)
    print(str(Music_Name))          #(e.g)str1 = "Hello World"     print(str(str1))  O/P:- Hello World
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

frameCnt = 30
frames = [PhotoImage(file='D:\__pycache__\music2.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)

# icon
lower_frame=Frame(root,bg="white", width=485, height=180)
lower_frame.place(x=0, y=400)

image_icon=PhotoImage(file="D:\__pycache__\logo.png")
root.iconphoto(False,image_icon)

Menu=PhotoImage(file="D:\__pycache__\menu.png")
Label(root,image=Menu).place(x=0, y=580, width=475, height=50)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)

#play button
ButtonPlay=PhotoImage(file="D:\__pycache__\play1.png")
Button(root, image=ButtonPlay, bg="white", bd=0, height=60, width=60, command=PlayMusic).place(x=215, y=467)

#stop button
ButtonStop=PhotoImage(file="D:\__pycache__\stop1.png")
Button(root, image=ButtonStop, bg="white", bd=0, height=60, width=60, command=mixer.music.stop).place(x=130, y=467)

#pause button
ButtonPause=PhotoImage(file="D:\__pycache__\pause1.png")
Button(root, image=ButtonPause, bg="white", bd=0, height=60, width=60, command=mixer.music.pause).place(x=300, y=467)


Button(root, text="Browse Music", width=59, height=1, font=("calibri", 12, "bold"), fg="Black", bg="#ffffff", command= AddMusic).place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Time new roman", 10),bg="grey", fg="white", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand= Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

root.mainloop()

