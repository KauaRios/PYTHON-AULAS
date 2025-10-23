import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()



        self.Entrada=ttk.Entry(self)
        self.Entrada.grid(row=0, column=0, padx=10, pady=10)

        self.button = ttk.Button(self, text="Mostrar o que foi Escrito",command=self.mostrar_descrito)
        self.button.grid(row=0, column=1, padx=10, pady=10)

        self.Label = ttk.Label(self,text="")
        self.Label.grid(row=1, column=0, padx=10, pady=10)




    def mostrar_descrito(self):
        digitado=self.Entrada.get()
        self.Label.config(text=f"Foi digitado: {digitado}")






root=tk.Tk()
app = App(master=root)
app.mainloop()