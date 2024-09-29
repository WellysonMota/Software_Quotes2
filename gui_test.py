import tkinter as tk
from tkinter import ttk
import datetime

# Data de hoje formatada
data = datetime.date.today()
data_formatada = data.strftime("%d%m%Y")

# Função de exemplo para chamar alerta
def call_alert(mensagem):
    messagebox.showinfo("Alerta", f"{mensagem}")

# Função de exemplo para obter valor do dólar
def on_button_click():
    # Placeholder para valor do dólar
    dolar_value = 5.36  # Substituir com a função que retorna o valor
    label = tk.Label(statusbar, text=f'O valor atual do Dólar é: R$ {dolar_value}')
    label.grid(row=0, column=2, padx=0, pady=0, sticky="w")

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerador de Cotações - EPS")
largura = 960
altura = 680
x = (janela.winfo_screenwidth() - largura) // 2
y = (janela.winfo_screenheight() - altura) // 2
janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Frame para organizar os elementos
toolbar = tk.Frame(janela, background="#d5e8d4", height=40)
statusbar = tk.Frame(janela, background="#e3e3e3", height=20)
main = tk.PanedWindow(janela, background="#fff")

toolbar.pack(side="top", fill="x")
statusbar.pack(side="bottom", fill="x")
main.pack(side="top", fill="both", expand=True)

left_pane = tk.Frame(main, background="#b2bbc2", width=100)
right_pane = tk.Frame(main, background="#f0f5f5", width=200)
main.add(left_pane)
main.add(right_pane)

# Criação de um Frame com Canvas para rolagem
canvas = tk.Canvas(right_pane, background="white")
canvas.place(x=0, y=440, relwidth=1, height=290)

# Frame para adicionar widgets no Canvas
scrollable_frame = tk.Frame(canvas, background="lightblue")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Scrollbar configurada para o Canvas
scrollbar = tk.Scrollbar(right_pane, orient="vertical", command=canvas.yview)
scrollbar.place(x=940, y=440, height=290)  # Ajuste a posição para alinhar à direita do Canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Atualizar o Canvas quando o Frame interno for redimensionado
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Adicionar widgets no Frame rolável
for i in range(20):
    tk.Label(scrollable_frame, text=f"Label {i}", bg="lightblue").pack(pady=10, padx=10)
    tk.Button(scrollable_frame, text=f"Button {i}").pack(pady=10, padx=10)

# Iniciar a janela principal
janela.mainloop()
