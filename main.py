from tkinter import *
from tkinter import ttk
from LinkedListView import *
import MergeSortView

root = Tk()
root.geometry("500x600")
root.title("Data Structures and Algorithms")

btnLinkedList = (Button(root, text="Linked List Demo", command= lambda:LinkedListView(root)).
                grid(row=4, column=2, padx=10, pady=10))

btnMergeSort = Button(root, text="Merge Sort Demo", command= lambda:MergeSortView(root))
btnMergeSort

root.mainloop()