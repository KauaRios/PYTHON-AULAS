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
