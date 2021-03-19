#from os import cpu_count
from tkinter import *
import pyshorteners

App = Tk()

class operacao():
    def encurtador(self):
        sht = pyshorteners.Shortener()
        gerarUrl = sht.tinyurl.short(str(self.get_url.get()))
        self.saida.insert(END, gerarUrl)

class Application(operacao):
    def __init__(self,):
        self.App = App
        self.conf_window()
        self.conf_frames()
        self.conf_itens()
        App.mainloop()
    
    def conf_window(self):
        self.App.title("Encurtador de Link")
        self.App.geometry("400x150")
        self.App.configure(background="#08ff00")
        self.App.resizable(False, False)

    def conf_frames(self):
        self.frame2 = Frame(self.App, background="#1C1C1C")
        self.frame2.place(relx=0.011, rely=0.025, relwidth=0.98, relheight=0.94)

    def conf_itens(self):
        self.title1 = Label(self.frame2, text="Insira a URL", font="Arial 12 bold", background="#08ff00", width=15)
        self.title1.pack(side=TOP)

        self.get_url = Entry(self.frame2, width=55, border=2)
        self.get_url.pack(side=TOP)

        self.title2 = Label(self.frame2, text="Link", background="#08ff00")
        self.title2.pack(side=TOP)

        self.saida = Text(self.frame2, width=38, height=1.1, border=3)
        self.saida.pack(side=TOP)

        self.encurtar = Button(self.frame2, text="Encurtar", border=0, background="#4B5857", width=60, height=1, command=self.encurtador)
        self.encurtar.pack(side=BOTTOM)
       
Application()
