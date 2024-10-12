import tkinter as tk
from tkinter import messagebox

# Lista de produtos (array) com dicionários representando cada produto
produtos = [
    {"id": 1, "nome": "Transceiver 10G", "preco": 100},
    {"id": 2, "nome": "Transceiver 40G", "preco": 250},
    {"id": 3, "nome": "Transceiver 100G", "preco": 500},
    {"id": 4, "nome": "Cabo Óptico 10m", "preco": 75}
]


# Função que é chamada quando o botão é clicado
def verificar_produto():
    # Capturar o valor digitado na entrada
    valor_entrada = entrada.get()

    # Verificar se algum produto contém o valor digitado no nome
    produto_encontrado = None  # Variável para armazenar o produto encontrado
    for produto in produtos:
        if valor_entrada.lower() in produto["nome"].lower():  # Comparar ignorando maiúsculas/minúsculas
            produto_encontrado = produto
            break  # Interrompe a iteração quando o produto é encontrado

    # Estrutura if para tomar decisões com base no resultado da comparação
    if produto_encontrado:
        mensagem = f"Produto encontrado: {produto_encontrado['nome']} - Preço: ${produto_encontrado['preco']}"
        messagebox.showinfo("Produto Encontrado", mensagem)
    else:
        messagebox.showerror("Erro", "Produto não encontrado!")


# Criar a janela principal
root = tk.Tk()
root.title("Verificar Produto em Estoque")
root.geometry("400x200")

# Criar um campo de entrada (Entry) para digitação do nome do produto
entrada = tk.Entry(root, width=50)
entrada.pack(pady=20)

# Criar um botão que chama a função verificar_produto quando clicado
botao_verificar = tk.Button(root, text="Verificar Produto", command=verificar_produto)
botao_verificar.pack(pady=10)

# Iniciar a interface
root.mainloop()
