def calcular(vetor_faturamento):
    
    valores_validos = [faturamento for faturamento in vetor_faturamento if faturamento != 0]
    
    menor_faturamento = min(vetor)
    
    maior_faturamento = max(vetor)
    
    media_mensal = sum(valores_validos) / len(valores_validos) if valores_validos else None
    
    dias_acima_da_media = sum(1 for faturamento in vetor if faturamento > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media, media_mensal


vetor = [31490.7866, 37277.9400, 37708.4303, 0.0000, 0.0000, 17934.2269, 0.0000, 6965.1262, 24390.9374, 14279.6481, 0.0000, 0.0000, 39807.6622, 27261.6304, 39775.6434, 29797.6232, 17216.5017, 0.0000, 0.0000, 12974.2000, 28490.9861, 8748.0937, 8889.0023, 17767.5583, 0.0000, 0.0000, 3071.3283, 48275.2994, 10299.6761, 39874.1073]

menor, maior, dias_acima_media, media_men = calcular(vetor)

print("Média: ", media_men)
print("Menor faturamento:", menor)
print("Maior faturamento:", maior)
print("Dias com faturamento acima da média mensal:", dias_acima_media)