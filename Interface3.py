import tkinter as tk
from tkinter import ttk
from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image
from PIL import ImageTk
import time
import customtkinter

from tkinter_webcam import webcam

window = tk.Tk()
window.title("Interface")
window.geometry("1000x800")

video = webcam.Box(window, width=640, height=480)
video.show_frames()

# customtkinter.set_appearance_mode('dark')
# customtkinter.set_default_color_theme("dark-blue")

btn = Button(window, text='Start Video !', bd='5',
             command=window.destroy)
btn.pack(padx=15, pady=20)
btn.place(x=900,y=100)

btn = Button(window, text='Stop Video !', bd='5',
             command=window.destroy)
btn.place(x=900,y=150)

btn = Button(window, text='Pause Video !', bd='5',
             command=window.destroy)
btn.place(x=900,y=200)

tk.mainloop()