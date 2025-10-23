import tkinter as tk
from tkinter import ttk
from tokenize import String


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.nome_entrada = ttk.Entry(self)
        self.nome_entrada.grid(row=0, column=0, padx=10, pady=10)


        self.botao=ttk.Button(self,text="Mostrar Nome",command=self.mostrar_nome)
        self.botao.grid(row=0, column=1, padx=10, pady=10)


        self.label=ttk.Label(self,text="")
        self.label.grid(row=1, column=0, padx=10, pady=10)


    def mostrar_nome(self):
        nome=self.nome_entrada.get()
        self.label.config(text=f"Olá, {nome}")


root = tk.Tk()
root.title("Meu Aplicativo Que Faz Nada")
root.maxsize(1000, 400)

app = App(master=root)
app.mainloop()
