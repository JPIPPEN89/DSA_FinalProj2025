from tkinter import *
from tkinter import ttk
from LinkedListView import *

root = Tk()
root.geometry("500x600")
root.title("Data Structures and Algorithms")

btnLinkedList = (Button(root, text="Linked List Demo", command=lambda:LinkedListView(root)).
                grid(row=4, column=2, padx=10, pady=10))

root.mainloop()