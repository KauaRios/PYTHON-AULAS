import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pdfplumber
import re

def extrair_datas(texto):
    # Expressão regular para detectar datas nos formatos dd/mm/yyyy ou dd-mm-yyyy
    padrao = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(padrao, texto)

def ler_pdf(caminho):
    try:
        texto = ""
        with pdfplumber.open(caminho) as pdf:
            for pagina in pdf.pages:
                texto += pagina.extract_text() or ""  # Evita erro se a página não tiver texto
        return texto
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler o PDF: {str(e)}")
        return ""

def selecionar_pdf():
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if not caminho:
        return
    texto = ler_pdf(caminho)
    if not texto:
        return
    datas = extrair_datas(texto)
    if not datas:
        messagebox.showinfo("Nenhuma data encontrada", "Nenhuma data foi detectada no PDF.")
        return
    atualizar_tabela(datas)

def atualizar_tabela(datas):
    for item in tree.get_children():
        tree.delete(item)
    for data in datas:
        tree.insert("", "end", values=(data, "Aguardando verificação..."))

# --- Interface gráfica ---
janela = tk.Tk()
janela.title("Verificador de Feriados (PDFPlumber)")
janela.geometry("600x400")

frame = ttk.Frame(janela, padding=10)
frame.pack(fill="both", expand=True)

botao_pdf = ttk.Button(frame, text="Selecionar PDF", command=selecionar_pdf)
botao_pdf.pack(pady=5)

cols = ("Data", "Status")
tree = ttk.Treeview(frame, columns=cols, show="headings", height=10)
tree.column("Data", width=100)
tree.column("Status", width=150)
for col in cols:
    tree.heading(col, text=col)
tree.pack(fill="both", expand=True, pady=10)

# Barra de rolagem
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

janela.mainloop()
