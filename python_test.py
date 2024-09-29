import tkinter as tk

# Janela principal
root = tk.Tk()
root.title("Exemplo de Janela com Scroll")

# Frame principal
main_frame = tk.Frame(root, bg="gray", bd=5)
main_frame.pack(expand=True, fill="both")

# Frame para o conteúdo rolável
scroll_frame = tk.Frame(main_frame)
scroll_frame.pack(expand=True, fill="both")

# Canvas para criar a área rolável
canvas = tk.Canvas(scroll_frame, bg="white")
canvas.pack(side="left", fill="both", expand=True)

# Barra de rolagem vertical
scrollbar = tk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Frame interno para adicionar widgets dentro do canvas
scrollable_frame = tk.Frame(canvas, bg="lightblue")

# Adicionar o frame interno ao canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Configurar a rolagem do canvas com o frame interno
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.configure(yscrollcommand=scrollbar.set)

# Adicionar alguns widgets no frame interno
for i in range(20):  # Simulação de muitos widgets para ativar a rolagem
    tk.Label(scrollable_frame, text=f"Label {i}", bg="lightblue").pack(pady=10, padx=10)
    tk.Button(scrollable_frame, text=f"Button {i}").pack(pady=10, padx=10)

# Iniciar a janela
root.mainloop()
