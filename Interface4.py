import tkinter as tk
from tkinter import ttk
from tkinter import *
from typing import Optional, Union, Tuple

import cap as cap
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image
from PIL import ImageTk
import time
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("800*800")
app.title("Customtkinter Interface2")


class TimeIn(customtkinter.CTk):
    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 **kwargs):
        """

        :type kwargs: object
        """
        super().__init__(fg_color, *kwargs)
        self.camera = None

    def streaming(self):
        ret, img = cap.read()
        cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        ImgTks = ImageTk.PhotoImage(image=img)
        self.camera.imgtk = ImgTks
        self.camera.configure(image=ImgTks)
        self.after(20, self.streaming)


if __name__ == "__main__":
    app = TimeIn()
    app.streaming()
    app.mainloop()
