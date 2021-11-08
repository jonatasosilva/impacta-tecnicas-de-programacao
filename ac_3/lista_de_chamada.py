def le_nomes(n):
    nomes = []
    for i in range(n):
        nome = input()
        nomes.append(nome)

    return nomes


def main():
    n, k = input().split()

    nomes = le_nomes(int(n))
    nomes.sort()

    print(nomes[int(k)-1])


if __name__ == '__main__':
    main()
