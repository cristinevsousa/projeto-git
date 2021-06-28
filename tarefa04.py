# 4. Crie uma função para desenhar uma linha, usando o caractere '_' (underline).
# O tamanho da linha deve ser definido na chamada da função.

def linha(quant):
    n = ""
    for i in range(quant):
        i += 1
        n += "_"
    return n


valor = int(
    input("Digite o número de underlines para o tamanho da linha que deseja: "))
saida = linha(valor)
print(saida)
