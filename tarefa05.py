# 5. Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo.
# A função deve imprimir todos os elementos da lista, enumerando-os.

def enum(lista):
    for i in range(len(lista)):
        print(i+1, "-", lista[i])


lista = ["abc", 2, 3.5, True]

enum(lista)
