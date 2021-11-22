from benchmark import tempo
from math import sqrt, ceil


def pares_impares(numero, palavra, arquivo_saida):
    inicio = 0 if palavra == 'pares' else 1

    for i in range(inicio, numero+1, 2):
        arquivo_saida.write(f'{i}\n')


def eh_primo(numero):
    if numero % 2 == 0:
        return numero == 2

    raiz = ceil(sqrt(numero))
    for divisor in range(3, raiz+1, 2):
        if numero % divisor == 0:
            return False

    return True


def primos(numero, arquivo_saida):
    total_primos = 0
    i = 2
    while total_primos < numero:
        if eh_primo(i):
            arquivo_saida.write(f'{i}\n')
            total_primos += 1

        i += 1


def main():
    with open("entrada.txt", "r") as arquivo:
        palavra, numero = arquivo.readline().split()
        numero = int(numero)

    arquivo_saida = open('saida.txt', 'w')

    if palavra == 'pares' or palavra == 'impares':
        tempo_gasto = tempo(pares_impares, numero, palavra, arquivo_saida)
    if palavra == 'primos':
        tempo_gasto = tempo(primos, numero, arquivo_saida)

    arquivo_saida.write(f'Tempo = {tempo_gasto:.4f} segundos')
    arquivo_saida.close()


if __name__ == '__main__':
    main()
