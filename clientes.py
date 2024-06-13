import tkinter as tk
from tkinter import PhotoImage


class ClientesJanela:
    def __init__(self):
        self.janela_clientes = tk.Tk()
        self.janela_clientes.title("Consulta/Cadastro Clientes")
        self.janela_clientes.geometry("680x420")

        #self.global_image = PhotoImage(file="../files/lupa.png")
        self.button = tk.Button(self.janela_clientes, image=self.global_image, command="")
        self.button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.janela_clientes.mainloop()
