# 6. Crie um programa que converta horas em segundos,
# conforme o valor que o usuário informar quando solicitado a ele.

def conversor_segundos(num_horas):
    minutos_hora = num_horas * 60
    minutos = minutos_hora
    segundos = minutos * 60
    return segundos


valor_hora = int(
    input("Digite um valor inteiro para a quantidade de horas que deseja converter: "))
resultado = conversor_segundos(valor_hora)
print("O resultado da conversão é:", resultado, "segundos")
