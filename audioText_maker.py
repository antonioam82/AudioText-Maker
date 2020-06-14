from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as sct
from langs_dict import langs
import gtts
import threading
import os

class app():
    def __init__(self):
        self.window = Tk()
        self.window.title("AudioText Maker")
        self.window['bg'] = 'gainsboro'
        self.window.geometry("774x276")

        self.entry = sct.ScrolledText(self.window,width=69,height=8)
        self.entry.place(x=10,y=20)
        self.btnCreate = Button(self.window,text='CREATE AUDIO-TEXT',width=81)
        self.btnCreate.place(x=10,y=175)
        self.btnClear = Button(self.window,text='CLEAR TEXT',width=81)
        self.btnClear.place(x=10,y=205)
        self.btnTranslate = Button(self.window,text='TRANSLATE TEXT',width=81)
        self.btnTranslate.place(x=10,y=235)
        self.lang = 'en'
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

    def make_audio(self):
        self.lang = entryLang.get()
        self.tts = gtts.gTTS(self.entry.get(),lang=self.lang)
        self.tts.save("TextAudio.mp3")

    def insertb(self):
        for i in self.valores:
            self.entryLang.insert(END,i)

    def init_audio(self):
        t = threading.Thread(target=self.make_audio)

if __name__=="__main__":
    app()

