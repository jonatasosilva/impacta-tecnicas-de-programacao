def calcula_letalidade(idades):
    letalidade = 0
    while len(idades) > 1:
        soma_par = idades[0] - idades[-1]
        letalidade += soma_par
        idades.pop(0)
        idades.pop()

    return letalidade


def main():
    while True:
        try:
            quantidade_virus = int(input())
        except:
            break

        idades = input().split()
        idades = list(map(int, idades))
        idades.sort(reverse=True)

        letalidade = calcula_letalidade(idades)
        print(letalidade)


if __name__ == '__main__':
    main()
