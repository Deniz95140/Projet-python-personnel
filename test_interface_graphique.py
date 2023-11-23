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
