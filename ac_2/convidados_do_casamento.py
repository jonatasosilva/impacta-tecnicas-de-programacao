def imprime_lista(titulo, conjunto, eh_ultima_lista=False):
    print('--------------------')
    print(titulo)
    print('--------------------')

    lista = list(conjunto)
    lista.sort()
    for item in lista:
        print(item)

    if not eh_ultima_lista:
        print()


def main():
    convidados_pela_noiva = set()
    convidados_pelo_noivo = set()
    convidados_finais = set()
    convidados_apenas_pela_noiva = set()
    convidados_apenas_pelo_noivo = set()
    convidados_por_ambos = set()
    convidados_por_apenas_um_deles = set()

    while True:
        entrada = input()

        if entrada == 'ACABOU':
            break

        nome_convidado, convidado_pelo = entrada.split(';')

        if convidado_pelo == 'noiva':
            convidados_pela_noiva.add(nome_convidado)
        elif convidado_pelo == 'noivo':
            convidados_pelo_noivo.add(nome_convidado)

    convidados_finais = convidados_pela_noiva | convidados_pelo_noivo
    imprime_lista('LISTA FINAL', convidados_finais)

    convidados_apenas_pela_noiva = convidados_pela_noiva - convidados_pelo_noivo
    imprime_lista('APENAS NOIVA', convidados_apenas_pela_noiva)

    convidados_apenas_pelo_noivo = convidados_pelo_noivo - convidados_pela_noiva
    imprime_lista('APENAS NOIVO', convidados_apenas_pelo_noivo)

    convidados_por_ambos = convidados_pela_noiva & convidados_pelo_noivo
    imprime_lista('POR AMBOS', convidados_por_ambos)

    convidados_por_apenas_um_deles = convidados_pela_noiva ^ convidados_pelo_noivo
    imprime_lista('POR APENAS UM DELES', convidados_por_apenas_um_deles, True)


if __name__ == '__main__':
    main()

