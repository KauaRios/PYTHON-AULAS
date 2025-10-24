import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import re
import pdfplumber
import requests
from datetime import datetime

def extrair_datas(texto):
    if not texto:
        return []
    padrao = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(padrao, texto)

def ler_pdf(caminho):
    try:
        texto = ""
        with pdfplumber.open(caminho) as pdf:
            for pagina in pdf.pages:
                pagina_texto = pagina.extract_text()
                if pagina_texto:
                    texto += pagina_texto + "\n"
        return texto
    except Exception as e:
        raise RuntimeError(f"Erro ao ler PDF: {e}")

def atualizar_tabela(datas):
    for item in tree.get_children():
        tree.delete(item)
    for data in datas:
        tree.insert("", "end", values=(data, "Aguardando verificação..."))

def selecionar_pdf():
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if not caminho:
        return
    try:
        texto = ler_pdf(caminho)
    except Exception as e:
        messagebox.showerror("Erro ao abrir PDF", str(e))
        return
    datas = extrair_datas(texto)
    if not datas:
        messagebox.showinfo("Nenhuma data encontrada", "Nenhuma data foi detectada no PDF.")
        atualizar_tabela([])
        return
    datas_unicas = []
    for d in datas:
        if d not in datas_unicas:
            datas_unicas.append(d)
    atualizar_tabela(datas_unicas)
    botao_verificar.config(state="normal")

def buscar_feriados_ano(ano):
    try:
        url = f"https://date.nager.at/api/v3/PublicHolidays/{ano}/BR"
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        feriados = resposta.json()
        print(f"Feriados de {ano}:")
        for f in feriados[:3]:
            print(f"  - {f['date']} → {f['localName']}")
        return feriados
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro de conexão", f"Não foi possível conectar à API:\n{e}")
        return []
    except Exception as e:
        messagebox.showerror("Erro inesperado", str(e))
        return []

janela = tk.Tk()
janela.title("Verificador de Feriados - Commit 2")
janela.geometry("600x420")

frame = ttk.Frame(janela, padding=10)
frame.pack(fill="both", expand=True)

botao_pdf = ttk.Button(frame, text="Selecionar PDF", command=selecionar_pdf)
botao_pdf.pack(pady=6)

cols = ("Data", "Status")
tree = ttk.Treeview(frame, columns=cols, show="headings", height=12)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(fill="both", expand=True, pady=8)

botao_verificar = ttk.Button(frame, text="Verificar feriados", command=lambda: messagebox.showinfo("Info", "Função será adicionada no Commit 3."), state="disabled")
botao_verificar.pack(pady=6)

label_info = ttk.Label(frame, text="Formato procurado: dd/mm/YYYY. Clique em 'Selecionar PDF' para começar.")
label_info.pack(pady=4)

janela.mainloop()
