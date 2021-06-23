# 2. Faça um programa que leia 4 valores, calcule a média e imprima positivo ou negativo
# (para ser positivo a média deve ser acima de 1)

numeros = [1, 2, 3, 4]

print("A média de todos os valores é: ", (sum(numeros)/4))

if (sum(numeros)/4) <= 1:
    print("A média dos valores é negativa")
else:
    print("A média dos valores é positiva")
