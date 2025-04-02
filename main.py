import tkinter as tk


import tkinter as tk

# Model
class Model:
    def __init__(self):
        self.data = ""

    def set_data(self, text):
        self.data = text

    def get_data(self):
        return self.data

# View Tk opens the window
class View(tk.Tk):
    def __init__(self, controller):
        super().__init__() #super() is the parent functions rules

        self.controller = controller
        self.title("MVC Tkinter Example")
        self.geometry("400x200")  # Increased window size

        # Widgets these are the buttons and controls
        self.label = tk.Label(self, text="Enter text below:")
        self.label.pack(pady=5) # pady is pad y, on y axis

        self.tbxDataEntry = tk.Entry(self) #Entry is the text box
        self.tbxDataEntry.pack(pady=5)

        self.tbxDataEntry2 = tk.Entry(self)  # Entry is the text box
        self.tbxDataEntry2.pack(pady=5)
                                                            #command is the function
        self.btnButton = tk.Button(self, text="Move Text", command=self.controller.move_text)
        self.btnButton.pack(pady=5)

        self.lblResult = tk.Label(self, text="")
        self.lblResult.pack(pady=5)

    def get_entry_text(self):
        return self.tbxDataEntry.get()

    def update_label(self, text):
        self.lblResult.config(text=text)

    def update_entry(self, text):
        self.tbxDataEntry2.insert(0, text)

# Controller
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def move_text(self):
        text = self.view.get_entry_text()
        self.model.set_data(text)
        self.view.update_label(self.model.get_data())
        self.view.update_entry(text)

    def run(self):
        self.view.mainloop()

# Run the application
if __name__ == "__main__":
    app = Controller()
    app.run()
