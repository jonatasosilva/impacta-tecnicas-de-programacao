def le_nomes(tamanho_lista):
    nomes = []
    for i in range(tamanho_lista):
        nome = input()
        nomes.append(nome)

    return nomes


def conta_comportamento(nomes):
    total_comportadas = 0
    total_nao_comportadas = 0

    for nome in nomes:
        if '+' in nome:
            total_comportadas += 1
        elif '-' in nome:
            total_nao_comportadas += 1

    return total_comportadas, total_nao_comportadas


def remove_comportamento(nomes):
    nomes_sem_comportamento = []
    for nome in nomes:
        nome_sem_comportamento = nome.replace('+ ', '').replace('- ', '')
        nomes_sem_comportamento.append(nome_sem_comportamento)

    return nomes_sem_comportamento


def imprime_nomes_ordanados(nomes):
    nomes_sem_comportamento = remove_comportamento(nomes)
    nomes_ordenados = sorted(nomes_sem_comportamento)
    for nome in nomes_ordenados:
        print(nome)


def main():
    tamanho_lista = int(input())
    nomes = le_nomes(tamanho_lista)

    total_comportadas, total_nao_comportadas = conta_comportamento(nomes)

    imprime_nomes_ordanados(nomes)

    print(
        f'Se comportaram: {total_comportadas} | Nao se comportaram: {total_nao_comportadas}')


if __name__ == '__main__':
    main()
