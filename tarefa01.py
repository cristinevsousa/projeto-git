# 1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista;
# b) maior valor da lista;
# c) menor valor da lista;
# d) soma de todos os elementos da lista;
# e) lista em ordem crescente;
# f) lista em ordem decrescente.

lista = [5, 7, 2, 9, 4, 1, 3]

print("Lista Original:", lista)

print("Tamanho da lista:", len(lista))

print("Maior valor da lista:", max(lista))

print("Menor valor da lista:", min(lista))

print("Soma de todos os valores da lista:", sum(lista))

print("Lista em ordem crescente:", sorted(lista))

lista.sort(reverse=True)
print("Lista em ordem decrescente:", lista)
