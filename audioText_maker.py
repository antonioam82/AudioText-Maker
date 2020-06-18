from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import tkinter.scrolledtext as sct
from langs_dict import langs
import gtts
import threading
from googletrans import Translator
import os

class app():
    def __init__(self):
        self.window = Tk()
        self.window.title("AudioText Maker")
        self.window['bg'] = 'gainsboro'
        self.window.geometry("774x276")
        self.translator = Translator()
        self.translation = ""
        self.step1 = False
        self.text = ""        

        self.entry = sct.ScrolledText(self.window,width=69,height=8)#8
        self.entry.place(x=10,y=20)
        self.btnCreate = Button(self.window,text='CREATE AUDIO-TEXT',width=81,command=self.init_audio)
        self.btnCreate.place(x=10,y=175)
        self.btnTranslate = Button(self.window,text='TRANSLATE TEXT',width=81,command=self.init_translation)
        self.btnTranslate.place(x=10,y=205)
        self.btnClear = Button(self.window,text='CLEAR TEXT',width=81,command=self.clear)
        self.btnClear.place(x=10,y=235)
        self.scrollbar = Scrollbar(orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.entryLang = Listbox(self.window,width=26,height=15)
        self.entryLang.place(x=594,y=20)
        self.entryLang.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.entryLang.yview)
        self.label = Label(self.window,text="",width=81,bg='gainsboro',fg='red')
        self.label.place(x=10,y=154)
        
        self.valores = list(langs.values())
        self.claves = list(langs.keys())

        self.insertb()

        self.window.mainloop()
        
    def translate(self):
        try:
            self.label.configure(text='TRASLATING...')
            self.text = self.entry.get('1.0',END)
            self.entry.delete('1.0',END)
            self.position = (self.entryLang.curselection())[0]
            self.step1 = True
            self.lang = self.claves[(self.valores).index(self.entryLang.get(int(self.position)))] #self.entryLang.get(2)
            self.translation = (self.translator.translate(self.text,dest=self.lang).text)
            self.entry.insert(END,self.translation)
            self.step1 = False
        except:
            if self.step1 == False:
                messagebox.showwarning("ERROR","Make sure you have chosen a language")
            else:
                messagebox.showwarning("ERROR","Unexpected error")
        self.label.configure(text="")

    def clear(self):
        self.entry.delete('1.0',END)

    def make_audio(self):
        self.lang = self.lang
        myFile=filedialog.asksaveasfilename(initialdir="/",title="Save as",defaultextension=".mp3")
        self.tts = gtts.gTTS(self.translation,lang=self.lang)
        self.tts.save(myFile)
        messagebox.showinfo("TASK COMPLETED","File created successfully")
        
    def insertb(self):
        for i in self.valores:
            self.entryLang.insert(END,i)

    def init_translation(self):
        if len(self.entry.get('1.0',END))>1:
            t1 = threading.Thread(target=self.translate)
            t1.start()
        else:
            messagebox.showwarning("NO TEXT","You haven't wrote anything to translate")

    def init_audio(self):
        if self.translation != "":
            t = threading.Thread(target=self.make_audio)
            t.start()

if __name__=="__main__":
    app()

