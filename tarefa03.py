# 3. Escreva um programa que leia 20 valores inteiros e informe a média deles, o maior e o menor valor

print("Digite uma sequência de 20 números inteiros utilizando enter para adicionar cada um:")
numeros_lista = []
soma = 0
max_ = 0
min_ = 0

while len(numeros_lista) < 20:        
            for i in range(20):
                  
                numero = int(input())
                soma += numero    

                if i == 0:
                    min_ = numero

                if numero > max_:
                    max_ = numero

                if numero < min_:
                    min_ = numero
                    
                numeros_lista.append(numero)
                    
                if i != 19:
                    print("Você digitou o número: ", numero, " na posição: ", i+1)
                    print("Digite o próximo número")
                else:
                    print("Pronto!")
                    print()


print("Resultado:", numeros_lista)
print()
print("A média de todos os valores é: ", (soma/20))
print()
print("O maior valor da lista é:", max_)
print()
print("O menor valor da lista é:", min_)
