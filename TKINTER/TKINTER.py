import tkinter as tk
from tkinter import ttk
from tokenize import String


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.tk_label = ttk.Label(self, text="Hello world")
        self.tk_label.pack()



root = tk.Tk()
app=Application(master=root)
app.mainloop()


