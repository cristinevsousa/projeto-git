# 1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista;
# b) maior valor da lista;
# c) menor valor da lista;
# d) soma de todos os elementos da lista;
# e) lista em ordem crescente;
# f) lista em ordem decrescente.

lista = [5, 7, 2, 9, 4, 1, 3]
max_ = 0
min_ = lista[0]
total_lista = 0
soma = 0
lista_crescente = []
lista_decrescente = []

print("Lista Original:", lista)

for i in lista:
    soma += i
    total_lista += 1

for i in range(total_lista):
            
    if lista[i] < min_:
        min_ = lista[i]

    if lista[i] > max_:
        max_ = lista[i]

print("Tamanho da lista:", total_lista)
print("Menor valor da lista:", min_)
print("Maior valor da lista:", max_)
print("Soma de todos os valores da lista:", soma)

for i in range(total_lista):
        
    for j in range(total_lista):
            
        if lista[i] < lista[j]:

            ordem = lista[i]
            lista[i] = lista[j]
            lista[j] = ordem


lista_crescente = lista

print("Lista em ordem crescente:", lista_crescente)


for i in range(total_lista):
        
    for j in range(total_lista):
            
        if lista[i] > lista[j]:

            ordem = lista[i]
            lista[i] = lista[j]
            lista[j] = ordem

lista_decrescente = lista

print("Lista em ordem decrescente:", lista_decrescente)












