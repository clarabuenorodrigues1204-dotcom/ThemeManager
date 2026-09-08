def escolha_tema(interface_temas):
    titulo = "THEMES MANAGER"
    print(f'{titulo:-^40}')

    for i, tema in enumerate(interface_temas, start=1):
        print(f'[{i}] - {tema}')

    while True:
        try:
            opcao_usuario = int(input('\nQual é a opção desejada? '))
            print('-' * 40)

            if 1 <= opcao_usuario <= len(interface_temas):
                tema_escolhido = list(interface_temas)[opcao_usuario - 1]
                
                return tema_escolhido

            print('Opção inválida!')

        except ValueError:
            print('Digite apenas números.')