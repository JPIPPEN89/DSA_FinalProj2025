import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import LinkedListController as llc
#import Student as std

class LinkedListView(Toplevel):

    def __init__(self, rootWindow):
        Toplevel.__init__(self)
        self.controller = llc.LinkedListController()

        self.title("Linked List Demo")
        self.geometry("900x800")

        frameLeft = Frame(self, width=30, height=40, highlightbackground="black", highlightthickness=2)
        frameLeft.pack(side=LEFT, padx=20, pady=20)

        frameRight = Frame(self, width=70, height=40, highlightbackground="black", highlightthickness=2)
        frameRight.pack(side=RIGHT, padx=20, pady=20)

        self.lblStudentList = ttk.Label(frameLeft, text="Current Student List").grid(row=1, column=0, padx=10, pady=0)
        self.tboxData = tk.Text(frameLeft, width=30, height=20)
        self.tboxData.grid(row=2, column=0)


 # Student information data entry
        self.lblFirstName = ttk.Label(frameRight, text="First Name:").grid(row=1, column=0, padx=10, pady=0)
        self.entFirstName = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entFirstName.grid(row=1, column=1, padx=10, pady=10)

        self.lblLastName = ttk.Label(frameRight, text="Last Name:").grid(row=2, column=0, padx=10, pady=0)
        self.entLastName = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entLastName.grid(row=2, column=1, padx=10, pady=10)

        self.lblSSN = ttk.Label(frameRight, text="SSN:").grid(row=3, column=0, padx=10, pady=0)
        self.entSSN = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entSSN.grid(row=3, column=1, padx=10, pady=10)

        self.lblPhone = ttk.Label(frameRight, text="Phone:").grid(row=4, column=0, padx=10, pady=0)
        self.entPhone = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entPhone.grid(row=4, column=1, padx=10, pady=10)

        self.lblEmail = ttk.Label(frameRight, text="Email:").grid(row=5, column=0, padx=10, pady=0)
        self.entEmail = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entEmail.grid(row=5, column=1, padx=10, pady=10)

#Buttons

        self.btnAppend =  ttk.Button(frameRight, text="Append",
             command=lambda:[
                 self.controller.append(self.entFirstName.get(), self.entLastName.get(), self.entSSN.get(), self.entPhone.get(), self.entEmail.get()),
                 self.updateDisplay()
             ])
        self.btnAppend.grid(row=7, column=0, padx=10, pady=10)

        self.btnPrepend = ttk.Button(frameRight, text="Prepend",
                                    command=lambda: [
                 self.controller.prepend(self.entFirstName.get(), self.entLastName.get(),
                    self.entSSN.get(), self.entPhone.get(),
                    self.entEmail.get()),self.updateDisplay()])

        self.btnPrepend.grid(row=7, column=1, padx=10, pady=10)

        self.btnDisplay = ttk.Button(frameRight, text="Display Data", command=self.updateDisplay())
        self.btnDisplay.grid(row=8, column=0,padx=10,pady=10)

        self.btnClear = ttk.Button(frameRight, text="Clear the Data", command=lambda:[self.tboxData.delete("1.0", tk.END)])
        self.btnClear.grid(row=8, column=1, padx=10, pady=1)

        self.btnLoadFile = ttk.Button(frameRight, text="Open", command=lambda:[self.getFile()])
        self.btnLoadFile.grid(row=9, column=0, padx=10, pady=10)

        self.lblStatus = ttk.Label(frameLeft, text="")
        self.lblStatus.grid(row=5, column=0, padx=10, pady=10)

        self.lblInstruction = ttk.Label(frameRight, text="Enter SSN above to delete or search")
        self.lblInstruction.grid(row=10, column=0, columnspan=2,padx=0, pady=0)

        self.btnDelete = ttk.Button(frameRight, text="Delete",
                command=lambda:[
                self.controller.delete(self.entSSN.get()),
                self.updateDisplay()])
#View Methods
    def updateDisplay(self):
        self.tboxData.delete("1.0", tk.END)
        self.tboxData.insert(INSERT, self.controller.display())

    def getFile(self):
        fileName = filedialog.askopenfile(title="", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
        row_count = self.controller.load(fileName)
        self.lblStatus.config(text="Students Loaded: " + str(row_count))
        self.updateDisplay()