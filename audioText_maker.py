from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as sct
import gtts
import os

class app():
    def __init__(self):
        self.window = Tk()
        self.window.title("AudioText Maker")
        self.window.geometry("700x500")


        self.window.mainloop()

if __name__=="__main__":
    app()
