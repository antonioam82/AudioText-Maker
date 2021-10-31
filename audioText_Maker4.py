#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import tkinter.scrolledtext as sct
import gtts, playsound
import threading
from googletrans import Translator
import os

langs ={'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan', 'hr': 'Croatian',
        'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino','fi': 'Finnish','fr': 'French',
        'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'hi': 'Hindi', 'hu': 'Hungarian', 'is': 'Icelandic', 'id': 'Indonesian', 'it': 'Italian',
        'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'km': 'Khmer', 'ko': 'Korean', 'la': 'Latin', 'lv': 'Latvian', 'mk': 'Macedonian',
        'ml': 'Malayalam', 'mr': 'Marathi', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'pl': 'Polish',
        'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sr': 'Serbian', 'si': 'Sinhala', 'sk': 'Slovak', 'es': 'Spanish', 'su': 'Sundanese',
        'sw': 'Swahili', 'sv': 'Swedish', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu',
        'vi': 'Vietnamese', 'cy': 'Welsh', 'zh-cn': 'Chinese (Mandarin/China)', 'zh-tw': 'Chinese (Mandarin/Taiwan)'}

class app():
    def __init__(self):
        self.window = Tk()
        self.window.title("AudioText Maker")
        self.window['bg'] = 'gainsboro'
        self.window.geometry("785x299")
        self.translator = Translator()
        self.myFile = ""
        self.translation = ""
        self.text = ""
        self.lang = ""
        self.canvas = Canvas(self.window)
        self.canvas.place(x=598,y=40)
        self.ultimo = ""
        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())

        Entry(self.window,textvariable=self.currentDir,width=130).place(x=0,y=0)
        self.entry = sct.ScrolledText(self.window,width=69,height=8,bg='azure1')
        self.entry.place(x=10,y=40)
        Button(self.window,text='CREATE AUDIO-TEXT',width=81,bg='thistle2',command=self.init_audio).place(x=10,y=195)
        Button(self.window,text='TRANSLATE TEXT',width=81,bg='thistle2',command=self.init_translation).place(x=10,y=225)
        Button(self.window,text='CLEAR TEXT',width=39,bg='thistle2',command=self.clear).place(x=10,y=255)
        Button(self.window,text='LISTEN AUDIO-FILE',width=39,bg='thistle2',command=self.init_playsound).place(x=304,y=255)
        self.scrollbar = Scrollbar(self.canvas,orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.entryLang = Listbox(self.canvas,width=26,height=15)
        self.entryLang.pack()
        self.entryLang.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.entryLang.yview)
        self.label = Label(self.window,text="",width=81,bg='gainsboro',fg='blue')
        self.label.place(x=10,y=174)
        
        self.valores = list(langs.values())
        self.claves = list(langs.keys())

        self.insertb()

        self.window.mainloop()
        
    def translate(self):
        try:
            self.label.configure(text='TRASLATING...')
            self.define_lang()
            self.text = self.entry.get('1.0',END)
            self.entry.delete('1.0',END)
            self.position = (self.entryLang.curselection())[0]
            self.lang = self.claves[(self.valores).index(self.entryLang.get(int(self.position)))] 
            self.translation = (self.translator.translate(self.text,dest=self.lang).text)
            
        except Exception as e:
            if str(e) == "tuple index out of range":
                messagebox.showwarning("ERROR","Make sure you have chosen a language.")
            else:
                print(str(e))
                messagebox.showwarning("ERROR",("Unexpected error: "+str(e)))

        self.label.configure(text="")
        self.insert_translation()

    def play_audio(self):
        try:
            self.label.configure(text='PLAYING: {}'.format((self.ultimo).split("/")[-1]))
            playsound.playsound(self.ultimo)
        except:
            messagebox.showwarning("ERROR",'Can not play {}'.format((self.ultimo).split("/")[-1]))
        self.label.configure(text="")
        

    def clear(self):
        self.entry.delete('1.0',END)

    def insert_translation(self):
        if self.translation != "":
            self.entry.insert(END,self.translation)

    def make_audio(self):
        self.myFile=filedialog.asksaveasfilename(initialdir="/",title="Save as",initialfile="audiotext",defaultextension=".mp3")
        if self.myFile != "":
            self.ultimo = self.myFile
            self.label.configure(text="CREATING AUDIO FILE")
            try:
                self.define_lang()
                if self.translation == self.entry.get('1.0',END):
                    self.tts = gtts.gTTS(self.translation,lang=self.lang)
                else:
                    lan = (self.translator.translate(self.entry.get('1.0',END)).src)
                    self.tts = gtts.gTTS(self.entry.get('1.0',END),lang=lan)
                self.tts.save(self.myFile)
                messagebox.showinfo("TASK COMPLETED","File created successfully.")
            except Exception as e:
                messagebox.showwarning("ERROR","Unexpected error: "+str(e))
                print(str(e))
            self.label.configure(text="")
            self.lang = ""
            self.translation = ""

    def define_lang(self):
        if self.lang == "":
            self.lang = (self.translator.translate(self.entry.get('1.0',END)).src)
            self.translation = self.entry.get('1.0',END)
        
    def insertb(self):
        for i in self.valores:
            self.entryLang.insert(END,i)

    def init_translation(self):
        if len(self.entry.get('1.0',END))>1:
            t1 = threading.Thread(target=self.translate)
            t1.start()
        else:
            messagebox.showwarning("NO TEXT","You haven't written anything to translate.")

    def init_audio(self):
        if len(self.entry.get('1.0',END))>1:
            t = threading.Thread(target=self.make_audio)
            t.start()

    def init_playsound(self):
        if self.ultimo != "":
            t1 = threading.Thread(target=self.play_audio)
            t1.start()
        else:
            messagebox.showwarning("NO FILE CREATED","You haven't created your audio file yet.")

if __name__=="__main__":
    app()
