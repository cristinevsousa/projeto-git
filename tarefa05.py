# 5. Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo.
# A função deve imprimir todos os elementos da lista, enumerando-os.

def enum(lista):
    i = 0
    while i < len(lista):
        print(i+1, "-", lista[i])
        i += 1


lista = ["abc", 2, 3.5, True]

enum(lista)
