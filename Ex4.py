def calcular(valor_estado, valor_total):
    return (valor_estado / valor_total) * 100

faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

valor_total = sum(faturamento_estados.values())

percentuais = {estado: calcular(valor, valor_total) for estado, valor in faturamento_estados.items()}

print("Percentual cada estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")