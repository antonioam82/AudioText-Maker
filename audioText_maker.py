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
        self.window['bg'] = 'gainsboro'
        self.window.geometry("773x430")

        self.entry = sct.ScrolledText(self.window,width=69,height=8)
        self.entry.place(x=10,y=20)
        self.btnTrans = Button(self.window,text='TRANSLATE')
        self.btnTrans.place(x=10,y=225)
        self.entryLang = ttk.Combobox(self.window,width=24,state='readonly')
        self.entryLang.place(x=594,y=20)


        self.window.mainloop()

if __name__=="__main__":
    app()
