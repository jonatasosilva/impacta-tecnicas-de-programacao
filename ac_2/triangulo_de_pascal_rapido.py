def pascal(linha, coluna, memo={}):
    if coluna == 1 or linha == coluna:
        return 1

    coordenada = (linha, coluna)

    if coordenada not in memo:
        memo[coordenada] = pascal(linha - 1, coluna) + \
            pascal(linha - 1, coluna - 1)

    return memo[coordenada]


def main():
    coordenadas = input()

    linha, coluna = coordenadas.split()

    valor_item = pascal(int(linha), int(coluna))
    print(valor_item)


if __name__ == '__main__':
    main()
