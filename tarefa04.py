# 4. Crie uma função para desenhar uma linha, usando o caractere '_' (underline).
# O tamanho da linha deve ser definido na chamada da função.

#Alternativa 1
def linha(quant):
    underline = ""
    for i in range(quant):
        i += 1
        underline += "_"
    return underline


valor = int(
    input("Digite o número de underlines para o tamanho da linha que deseja: "))
saida = linha(valor)
print(saida)



#Alternativa 2
def linha(quant):
    underline = ""
    i = 0
    while i < quant:
        i += 1
        underline += "_"
    return underline


valor = int(input("Digite um valor para o tamanho da linha que deseja: "))
saida = linha(valor)
print(saida)
