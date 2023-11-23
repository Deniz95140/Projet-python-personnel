import tkinter
from tkinter import messagebox

def messagea():
    messagebox.showinfo("Message", "Ceci est le bouton A.")

def messageb():
    messagebox.showinfo("Message", "Ceci est le bouton B.")

interface = tkinter.Tk()
interface.title("Boutons")

buttonA = tkinter.Button(interface, text="Bouton A", command=messagea)
buttonB = tkinter.Button(interface, text="Bouton B", command=messageb)

buttonA.pack()
buttonB.pack()

interface.mainloop()

import tkinter
from tkinter import messagebox

def messagea():
    messagebox.showinfo("Message", "Ceci est le bouton A.")

def messageb():
    messagebox.showinfo("Message", "Ceci est le bouton B.")

interface = tkinter.Tk()
interface.title("Boutons")

buttonA = tkinter.Button(interface, text="Bouton A", command=messagea)
buttonB = tkinter.Button(interface, text="Bouton B", command=messageb)

buttonA.pack()
buttonB.pack()

interface.mainloop()

'''
# POO:

class Interface:
    def __init__(self, root, boutona, boutonb):
        self.root = tkinter.Tk()
        self.root.title("Boutons")
        self.boutona = tkinter.Button(interface, text="Bouton A", command=self.messagea)
        self.boutonb = tkinter.Buton(interface, text="Bouton B", command=self.messageb)
        self.boutona.pack()
        self.boutonb.pack()

    def messagea(self):
        messagebox.showinfo("Message", "Ceci est le bouton A.")
    
    def messageb(self):
        messagebox.showinfo("Message", "Ceci est le bouton B.")

    def demarrer(self):
        self.root.mainloop()
    
interface = Interface()
interface.demarrer()
'''
