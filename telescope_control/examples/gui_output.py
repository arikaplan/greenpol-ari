from tkinter import ttk
#import tkinter as tk
#from tkinter.scrolledtext import ScrolledText
from tkinter import *


class ArisButtons:

    def __init__(self, master):    

        topframe = Frame(master)
        topframe.pack(side=TOP)

        bottomframe = Frame(master)
        bottomframe.pack(side=BOTTOM)

        self.label_1 = Label(topframe, text='number 1')
        self.label_1.grid(row = 0, column = 0)
        self.label_2 = Label(topframe, text='number 2')
        self.label_2.grid(row = 1, column = 0)

        #user input
        self.entry_1 = Entry(topframe)
        self.entry_1.insert(END, '5.0')
        self.entry_1.grid(row = 0, column = 1)
        self.entry_2 = Entry(topframe)
        self.entry_2.insert(END, '5.0')
        self.entry_2.grid(row = 1, column = 1)

        self.label_3 = Label(topframe, text='n1 + n2')
        self.label_3.grid(row = 2, column = 0, sticky = E)

        self.txt = Text(topframe, height = 1, width = 15)
        self.txt.grid(row = 2, column = 1)

        self.printButton = Button(bottomframe, 
        text='Add numbers', 
        command=self.add)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(bottomframe, text='quit', command=master.quit)
        self.quitButton.pack(side=LEFT)


    def add(self):
        self.txt.delete('1.0', END)
        n1 = self.entry_1.get()
        n2 = self.entry_2.get()
        n1 = float(n1)
        n2 = float(n2)
        #print(n1 + n2)
        self.txt.insert('1.0',n1 + n2)

root = Tk()
root.title("tabs")

b = ArisButtons(root)

root.mainloop()

