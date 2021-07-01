# 2. Faça um programa que leia 4 valores, calcule a média e imprima positivo ou negativo
# (para ser positivo a média deve ser acima de 1)

print("Digite uma sequência de 4 números inteiros utilizando enter para adicionar cada um:")
lista = []
soma = 0

while len(lista) < 4:        
            for i in range(4):

                numero = int(input())
                soma += numero
                lista.append(numero)

                if i != 3:
                    print("Você digitou o número: ", numero, " na posição: ", i+1)
                    print("Digite o próximo número")
                else:
                    print("Pronto!")
                    print()

print("A média de todos os valores é: ", (soma/4))
print()

if (soma/4) <= 1:
    print("A média dos valores é negativa")
else:
    print("A média dos valores é positiva")
