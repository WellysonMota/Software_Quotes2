import tkinter as tk
from tkinter import messagebox

def adicionar_item():
    """Adiciona um novo item à lista."""
    item = entrada_texto.get()
    if item:
        lista_box.insert(tk.END, item)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showinfo("Atenção", "Entrada vazia não é permitida!")

def remover_item():
    """Remove o item selecionado da lista."""
    try:
        index = lista_box.curselection()[0]
        lista_box.delete(index)
    except IndexError:
        messagebox.showinfo("Atenção", "Por favor, selecione um item para remover.")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Cotações")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Entrada de texto para novos itens
entrada_texto = tk.Entry(frame, width=50)
entrada_texto.pack(side=tk.TOP, padx=5, pady=5)

# Botões para adicionar e remover itens
botao_adicionar = tk.Button(frame, text="Adicionar Item", command=adicionar_item)
botao_adicionar.pack(side=tk.LEFT, padx=5, pady=5)

botao_remover = tk.Button(frame, text="Remover Item", command=remover_item)
botao_remover.pack(side=tk.RIGHT, padx=5, pady=5)

# Lista para mostrar os itens
lista_box = tk.Listbox(frame, width=50, height=10)
lista_box.pack(padx=5, pady=5)


