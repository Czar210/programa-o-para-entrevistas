funcionarios = [
    {"nome": "Ana", "depto": "Engenharia", "salario": 8000},
    {"nome": "Bruno", "depto": "Dados", "salario": 7000},
    {"nome": "Carla", "depto": "Engenharia", "salario": 9500},
    {"nome": "Diego", "depto": "Dados", "salario": 6500},
    {"nome": "Eva", "depto": "Engenharia", "salario": 7200},
]

def media_por_departamento(lista):
    acumulador = {}
    for funcionario in lista: 
        departamento = funcionario["depto"]
        if departamento not in acumulador:
            acumulador[departamento] = {"total": 0, "count": 0}
        acumulador[departamento]["total"] += funcionario["salario"]
        acumulador[departamento]["count"] += 1

        media = {departamento: acumulador[departamento]["total"] / acumulador[departamento]["count"] for departamento in acumulador}
    return media

print(media_por_departamento(funcionarios))
