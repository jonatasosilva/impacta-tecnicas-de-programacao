def le_casos(numero_casos):
    casos = []
    for caso in range(numero_casos):
        numero_alunos = int(input())
        notas = input().split()
        notas = list(map(int, notas))
        casos.append(notas)

    return casos


def imprime_numero_nao_trocas(casos):
    for caso in casos:
        notas = caso
        notas_ordenadas = sorted(notas, reverse=True)

        numero = 0
        for index, nota in enumerate(notas):
            if nota == notas_ordenadas[index]:
                numero += 1

        print(numero)


def main():
    numero_casos = int(input())
    casos = le_casos(numero_casos)
    imprime_numero_nao_trocas(casos)


if __name__ == '__main__':
    main()
