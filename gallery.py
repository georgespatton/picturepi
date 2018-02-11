#!/usr/bin/python3 

#Displays a loop of all image files found by gather_files.py.  Run that script first to populate your image db file.  See README for python dependency installation hints.

import tkinter as tk
from PIL import ImageTk, Image
import os, random, time

db = 'picture_db.txt'

#Open the db file and pick a random line to use as the displayed picture.
def get_random_file():
  file = open(db,'r')
  file_size = os.stat(db)[6]
  file.seek((file.tell()+random.randint(0,file_size-1))%file_size)
  file.readline()
  line = file.readline()
  return line.rstrip()

#Loop through a new image every 4 seconds.
def update_image():
  path = get_random_file()
  try:
    img = ImageTk.PhotoImage(Image.open(path).resize((800, 480))) 
  #Issue with image file, try another.
  except Exception as e:
    print("Error: " + str(e))
    path = get_random_file()
    img = ImageTk.PhotoImage(Image.open(path).resize((800, 480))) 
  panel.configure(image=img)
  panel.image = img
  window.after(4000, update_image)
  return

path = get_random_file()
window = tk.Tk()
window.attributes("-fullscreen",True)
window.title("Photo Gallery")
window.geometry("800x480")
window.configure(background='black')
#Load an initial image onto the Label.
try:
  img = ImageTk.PhotoImage(Image.open(path).resize((800, 480))) 
#Issue with image file, try another.
except Exception as e:
  print("Error: " + str(e))
  path = get_random_file()
  img = ImageTk.PhotoImage(Image.open(path).resize((800, 480))) 
panel = tk.Label(window, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

update_image()
window.mainloop()

