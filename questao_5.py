palavra = input("Escreva uma palavra: ")
palavra_lista = list(palavra)
tamanho = len(palavra_lista)
indice = -1
palavra_inverso = ''

while tamanho > 0:
    palavra_inverso += palavra_lista[indice]
    indice += -1
    tamanho += -1

print(palavra_inverso)
