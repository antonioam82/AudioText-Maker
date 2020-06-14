from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as sct
from langs_dict import langs
import gtts
import os

class app():
    def __init__(self):
        self.window = Tk()
        self.window.title("AudioText Maker")
        self.window['bg'] = 'gainsboro'
        self.window.geometry("774x276")

        self.entry = sct.ScrolledText(self.window,width=69,height=8)
        self.entry.place(x=10,y=20)
        self.btnTrans = Button(self.window,text='TRANSLATE')
        self.btnTrans.place(x=10,y=215)
        self.frame = Frame(self.window,bg='black')
        #self.frame.place(x=585,y=0)
        #self.frame.config(bg="lightblue")
        #self.frame.config(width=187,height=200)
     
        #self.entryLang = ttk.Combobox(self.frame,width=24,state='readonly')
        #self.entryLang.place(x=594,y=20)
        self.scrollbar = Scrollbar(orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        
        
        self.entryLang = Listbox(self.window,width=26,height=15)
        self.entryLang.place(x=594,y=20)
        
        self.entryLang.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.entryLang.yview)
        
        

        self.valores = list(langs.values())
        self.claves = list(langs.keys())

        self.insertb()

        self.window.mainloop()

    def insertb(self):
        for i in self.valores:
            self.entryLang.insert(END,i)

if __name__=="__main__":
    app()

