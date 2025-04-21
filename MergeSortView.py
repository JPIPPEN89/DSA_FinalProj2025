import MergeSortController as msc
import tkinter as tk
from tkinter import *
import MergeSortController as msc

class MergeSortView(Toplevel):

    def __init__(self, rootWindow):
        Toplevel.__init__(self)
        self.controller = msc.MergeSortController

        self.title("Merge Sort Demo")
        self.geometry("900x800")

        frameLeft = Frame(self, width=30, height=40, highlightbackground="black", highlightthickness=2)
        frameLeft.pack(side=LEFT, padx=20,pady=20)

        frameRight = Frame(self, width=70, height=60, highlightbackground="black", highlightthickness=2)
        frameLeft.pack(side=RIGHT, padx=20,pady=20)

        self.lablNumbersList = Label(frameLeft, text="Data List").grid(row=1, column=0, padx=10,pady=0)
        self.tboxData = Text(frameLeft, width=30,height=20)
        self.tboxData.grid(row=2, column=0)

        #Buttons
        self.btnLoad = Button(frameRight, text="Load Numbers", command= self.load)
        self.btnLoad.grid(row=0, column=0, padx=10, pady=10)

        self.btnDisplayNumbers = Button(frameRight, text="Display Numbers", command=self.display)
        self.btnDisplayNumbers.grid(row=1, column=0, padx=10, pady=10)




    def load(self):
        self.controller.load(10,100,1000)

    def display(self):
        self.tboxData.delete('1.0', END)
        numbers = self.controller.display()
        self.tboxData.insert(INSERT, numbers)
        self.controller.display()
