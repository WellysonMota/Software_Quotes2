

lista = [
    (1, "FTLX8574", "Finisar"),
    (2, "FTLX1672", "Finisar"),
    (3, "FTLF1318", "Finisar"),
    ]





substring = "FTLX"

for i in lista:
    if substring.lower() in i:
        print(i)
    else:
        print(f"Não há produtos com {substring}")
        break



def busca_simples():
    lista = [0, 1, 2, 4, 6, 12, 50, 20, 40, 70]

    for i in lista:
        if i > 10:
            print(i)


