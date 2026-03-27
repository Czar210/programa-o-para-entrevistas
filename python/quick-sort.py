
entrada = input()

lista_real = [int(item.strip()) for item in entrada[1:-1].split(",")]

def organizar_rapido(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    maiores, menores = [], []
    for i in range(1, len(lista)):
        if lista[i] < pivot:
            menores.append(lista[i])
        else:
            maiores.append(lista[i])
    return organizar_rapido(menores) + [pivot] + organizar_rapido(maiores)

print(organizar_rapido(lista_real)) 