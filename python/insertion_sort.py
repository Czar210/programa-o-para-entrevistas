
entrada = input()

lista_real = [int(item.strip()) for item in entrada[1:-1].split(",")]

def organizar_insert(lista): 
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
    return lista
print(organizar_insert(lista_real)) 