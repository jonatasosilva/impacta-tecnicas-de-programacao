def verifica_se_eh_par(numero):
    if numero == 0:
        return True

    if numero == 1:
        return False

    return verifica_se_eh_par(numero - 2)


def main():
    numero = int(input())

    eh_par = verifica_se_eh_par(numero)

    if eh_par:
        print('numero par')
    else:
        print('numero nao par')


if __name__ == '__main__':
    main()
