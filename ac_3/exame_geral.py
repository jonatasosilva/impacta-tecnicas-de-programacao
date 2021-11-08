def le_valores(numero):
    valores = []
    for i in range(numero):
        valor = int(input())
        valores.append(valor)

    return valores


def imprime_consultas(notas, consultas):
    notas.sort(reverse=True)

    for consulta in consultas:
        print(notas[consulta-1])


def main():
    while True:
        try:
            entrada = input()
            numero_habitantes, numero_consultas = entrada.split()
        except:
            break

        notas = le_valores(int(numero_habitantes))
        consultas = le_valores(int(numero_consultas))
        imprime_consultas(notas, consultas)


if __name__ == '__main__':
    main()
