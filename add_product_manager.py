import tkinter as tk
from tkinter import ttk




# Função para abrir a janela de pesquisa de produtos
def open_product_search():
    # Criar uma nova janela (popup)
    search_window = tk.Toplevel()
    search_window.title("Pesquisar Produtos")
    search_window.geometry("800x600")

    # Campo de pesquisa
    search_label = tk.Label(search_window, text="Pesquisar Produtos:")
    search_label.pack(pady=10)
    search_entry = tk.Entry(search_window, width=50)
    search_entry.pack(pady=5)

    # Combobox para filtro de categoria (exemplo: Transceivers, Cables, etc.)
    category_label = tk.Label(search_window, text="Categoria:")
    category_label.pack(pady=5)
    category_combobox = ttk.Combobox(search_window, values=["Transceivers", "Cables", "Switches"])
    category_combobox.pack(pady=5)

    # Treeview para mostrar resultados da pesquisa
    columns = ("ID", "Descrição", "Part Number", "Fabricante", "Preço", "Categoria")
    product_tree = ttk.Treeview(search_window, columns=columns, show="headings")
    product_tree.heading("ID", text="ID")
    product_tree.heading("Descrição", text="Descrição")
    product_tree.heading("Part Number", text="Part Number")
    product_tree.heading("Fabricante", text="Fabricante")
    product_tree.heading("Preço", text="Preço")
    product_tree.heading("Categoria", text="Categoria")

    # Ajustar largura das colunas
    product_tree.column("ID", width=40)
    product_tree.column("Descrição", width=250)
    product_tree.column("Part Number", width=100)
    product_tree.column("Fabricante", width=100)
    product_tree.column("Preço", width=100)
    product_tree.column("Categoria", width=100)

    # Adicionar Scrollbar para a Treeview
    scrollbar = ttk.Scrollbar(search_window, orient="vertical", command=product_tree.yview)
    product_tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Inserir alguns dados de exemplo
    products = [
        (1, "Transceiver 10G SFP+", "FTLX1471D3BCL", "Finisar", "$250", "Transceiver"),
        (2, "Transceiver 100G QSFP28", "FTL410QE2C", "Finisar", "$500", "Transceiver"),
        (3, "Transceiver 40G QSFP+", "FTL4E1QE1C", "Finisar", "$350","Transceiver"),
        (4, "Transceiver 40G QSFP+", "FT4S1QE2C", "Finisar", "$250", "Transceiver"),
        (5, "Transceiver 10G SFP+ SR", "XGXP-8596-02D", "X-Giga Amphenol", "$250", "Transceiver"),
    ]

    for product in products:
        product_tree.insert("", "end", values=product)




    # Posicionar Treeview
    product_tree.pack(expand=True, fill="both", padx=10, pady=10)

    # Botão para adicionar produto à cotação
    add_button = tk.Button(search_window, text="Adicionar à Cotação", command=lambda: add_to_quote(product_tree))
    add_button.pack(pady=10)


# Função para adicionar o produto à cotação
def add_to_quote(tree):
    selected_item = tree.selection()
    if selected_item:
        product = tree.item(selected_item)["values"]
        print(f"Produto Selecionado: {product}")  # Aqui você pode adicionar à cotação


