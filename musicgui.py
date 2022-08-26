import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()    # initialized with tkinter
canvas.title("Music Player")
canvas.geometry("600x600")
canvas.config(bg = 'black')

rootpath = ("C:\\Users\\Nupoor Gupta\\Music")   # single slash giving unicode error
pattern = "*.mp3"    # we'll match the pattern of the files inside this folder

mixer.init()        # initialize mixer

prev_img = tk.PhotoImage(file = "prev_img.png")    # initialize images PhotoImage is inbuilt func
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")    # image declaration
pause_img = tk.PhotoImage(file = "pause_img.png")
next_img = tk.PhotoImage(file = "next_img.png")
logo_img = tk.PhotoImage(file = "logo_img.png")

def select():
    label.config(text= listBox.get("anchor"))  #showing name inside the level, selected song inside get
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))  # to play song; with exact path
    mixer.music.play()     # play button

def stop():
    mixer.music.stop()     # stop currently playing music
    listBox.select_clear('active')    # clear selected song

def play_next():
    next_song = listBox.curselection()  # current selected song
    next_song = next_song[0] + 1   # index of next song
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)  # show next song name in level

    mixer.music.load(rootpath + "\\" + next_song_name)   # select next song
    mixer.music.play()        # play next song

    listBox.select_clear(0, 'end')    # selection gets clear
    listBox.activate(next_song)      # activate next song
    listBox.select_set(next_song)    # pass next song

def play_prev():
        next_song = listBox.curselection()
        next_song = next_song[0] - 1    # index for prev song
        next_song_name = listBox.get(next_song)
        label.config(text=next_song_name)

        mixer.music.load(rootpath + "\\" + next_song_name)
        mixer.music.play()

        listBox.select_clear(0, 'end')
        listBox.activate(next_song)
        listBox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":  # if song state is paused then we'll play
        mixer.music.pause()
        pauseButton["text"] = "PLay"  # if playing already we'll pause
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


logo = tk.Button(canvas, text="logo", image=logo_img, bg='black', borderwidth=0)
logo.pack(padx=10, pady=10, anchor='center')

listBox = tk.Listbox(canvas, fg = "dark green", bg = "black", width = 100, height = 12, font = ('cambria', 14))
listBox.pack(padx = 15, pady = 15)   # music listbox

label = tk.Label(canvas, text = '', bg = 'white', fg = 'black', font = ('cambria', 18))
label.pack(pady = 15)

top = tk.Frame(canvas, bg = "black")  # frame for buttons n so that can be horizontal
top.pack(padx = 10, pady = 5, anchor = 'center')     # anchor define text position relative to refrence pt

prevButton = tk.Button(canvas, text = "Prev", image = prev_img, bg = 'black', borderwidth = 0, command = play_prev)
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg='black', borderwidth=2, command= stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text="Play", image=play_img, bg='black', borderwidth=2, command = select)  # select func works
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text="Pause", image=pause_img, bg='black', borderwidth=2, command = pause_song)
pauseButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", image=next_img, bg='black', borderwidth= 0, command = play_next)
nextButton.pack(pady=15, in_=top, side='left')


for root, dirs, files in os.walk(rootpath):  # now all the files,directries of rootpath will run in this loop
    for filename in fnmatch.filter(files, pattern): # it will show all the matched files of same pattern
        listBox.insert('end', filename)  #all files adds in the end



canvas.mainloop()
