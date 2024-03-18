def inverte(palavra):
    invertida = palavra[::-1]
    return invertida

palavra = input('Digite uma palavra:\n')
invertida = inverte(palavra)
print(invertida)