lista_contatos = ['Petrônio', 'Pedro', 'Rudávia', 'Rafael']
agenda = 'sim'
while agenda == 'sim': 
    print("#####   Programa Agenda   #####")
    print()
    print("#  1 - Cadastrar contato      #")
    print("#  2 - Pesquisar contato      #")
    print("#  3 - Atualizar contato      #")
    print("#  4 - Apagar contato         #")
    print("#  5 - Listar todos           #")
    print("#  0 - Sair                   #")
    print()
    opcao = int(input('Digite a sua opção: '))
    print()
    while opcao != 0:
        if opcao == 1:
            qntd_pessoas = int(input('Informe a quantidade de pessoas que serão cadastradas: '))
            for i in range (qntd_pessoas):
                cadastrar = input('Digite o nome do seu novo contato: ').strip()
                lista_contatos.append(cadastrar)
            print(f'Essas são as pessoas que foram salvas no contato: {lista_contatos}')
        elif opcao == 2:
            qntd_pessoas = int(input('Informe a quantidade de pessoas que serão pesquisadas: '))
            for i in range(qntd_pessoas):
                pesquisar = input('Digite o nome do contato: ')
                print()
                if pesquisar in lista_contatos:
                    print('Esse contato está salvo na sua agenda')
                    print()
                else:
                    print('Esse contato não está salvo na sua agenda')
                    print()
                    salvar = input('Deseja salvar? ').strip().lower()
                    if salvar == 'sim': 
                        print()
                        lista_contatos.append(pesquisar)
                        print('O contato foi salvo com sucesso!')
                    else:
                        print('Obrigado pela consulta!')    
        elif opcao == 3:
            qntd_pessoas = int(input('Informe a quantidade de contatos que serão atualizados: '))
            for i in range (qntd_pessoas):
                atualizar = input('Qual o contato que deseja atualizar? ').strip()
                print()
                if atualizar in lista_contatos:
                    novo_nome = input('Digite o novo nome: ').strip()
                    print()
                    nome_antigo = lista_contatos.index(atualizar)
                    lista_contatos[nome_antigo] = novo_nome
                    
                else:
                    print('Nenhum nome encontrado')
            print('Lista atualizada: {}'.format(lista_contatos))
        elif opcao == 4:
            qntd_pessoas = int(input('Informe a quantidade de pessoas que serão removidas: '))
            for i in range(qntd_pessoas):
                remover_nome = input('Qual o contato que você deseja remover? ').strip()
                print()
                if remover_nome in lista_contatos:
                    lista_contatos.remove(remover_nome)
                    
                else:
                    print('Nome não encontrado')
            print('A lista foi atualizada e esses são os contatos que restam: {}'.format(lista_contatos))

        elif opcao == 5:
            print('Esses são todos os contatos salvos: {}'.format(lista_contatos))
        else: 
            print('Não existe essa função')
        break
    
        
    if opcao == 0: 
        print('Ao seu dispor!')
        print()
    agenda = input('Deseja entrar na sua agenda novamente? ').strip().lower()
    print()
print('Obrigado pela sua visita!')