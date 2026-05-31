lista_contatos = [['Pedro', '999868', 'pedro@gmail', '11'], ['Rafael', '999885', 'rafael@gmail', '18']]

agenda = 'sim'
resp = ''
while agenda == 'sim':
    print("################################")
    print("#####   Programa Agenda   #####")
    print("################################")
    print("#                              #")
    print("#  1 - Cadastrar contato       #")
    print("#  2 - Pesquisar contato       #")
    print("#  3 - Atualizar contato       #")
    print("#  4 - Apagar contato          #")
    print("#  5 - Listar todos            #")
    print("#  0 - Sair                    #")
    print("#                              #")
    print("#  Escolha sua opção:          #")
    print("################################")
        
    print()
    resp = int(input('Digite qual opção irá realizar: '))
    while resp != 0:
        if resp == 1:
            qntd_cont = int(input('Quantos contatos deseja cadastrar? '))
            for i in range(qntd_cont):
                print()
                nome = input('Digite o nome do seu contato: ').strip().title()
                telefone = input('Digite o número de telefone: ').strip()
                gmail = input('Digite o gmail do contato: ')
                idade = input('Digite a idade de seu contato: ')
                lista_contatos.append([nome,telefone,gmail,idade])
            print()
            print('A sua lista de contatos foi atualizada com sucesso!')
            print(f'Assim ficou ela: {lista_contatos}')
            break
        elif resp == 2:
            print()
            nome = input('Digite o nome do contato: ').strip().title()
            tam = len(lista_contatos)
            for i in range (tam):
                for j in range (3):
                    if nome in lista_contatos[i][j]:
                        print()
                        print('O contato está na lista')
                        print()
                        print(f'Nome: {lista_contatos[i][j]}')
                        print(f'Telefone: {lista_contatos[i][j+1]}')
                        print(f'Gmail: {lista_contatos[i][j+2]}')
                        print(f'Idade: {lista_contatos[i][j+3]} anos')
                    elif nome not in lista_contatos[i][j]:
                        print()
                        print('O contato não está salvo na lista')
                        print()
                        salvar = input('Deseja salvar? ').strip().lower()
                        while salvar == 'sim' or salvar == 's':
                            print()
                            telefone = input('Digite o número de telefone: ').strip()
                            gmail = input('Digite o gmail: ').strip()
                            idade = input('Digite a idade: ').strip()
                            lista_contatos.append([nome,telefone,gmail,idade])
                        print('Obrigado pela resposta')
        elif resp == 3:
            print()
            atualizar = input('Digite o contato que deseja atualizar: ').strip().title()
            tam = len(lista_contatos)
            for i in range(tam): 
                for j in range(3):
                    if atualizar in lista_contatos[i][j]:
                        print()
                        lista_contatos[i][j] = input('Digite o novo nome: ').strip().title()
                        print()
                        lista_contatos[i][j+1] = input('Digite o telefone: ').strip()
                        print()
                        lista_contatos[i][j+2] = input('Digite o Gmail: ').strip()
                        print()
                        lista_contatos[i][j+3] = input('Digite a idade do seu contato: ').strip()
                        print()
                        print('A sua lista foi atualizada com sucesso!')
                        print()
                        print(f'Assim ficou ela: {lista_contatos}')
                    elif atualizar not in lista_contatos[i][j]: 
                        print()
                        print('Esse contato não existe')
        elif resp == 4:
            print()
            tam = len(lista_contatos)
            contato_remover = input('Digite o contato que irá remover: ').strip().title()
            for i in range (tam): 
                    if contato_remover in lista_contatos[i]:
                        j = lista_contatos[i].index(contato_remover)
                        del lista_contatos[i][j]
                        del lista_contatos [i][j]
                        del lista_contatos [i][j]
                        del lista_contatos [i][j]
                        print()
                        print('A sua lista foi atualizada com sucesso')
                        print()
                        print(f'Assim ficou ela: {lista_contatos}')
                    else: 
                        print('Contato não encontrado')
        elif resp == 5:
            print()
            print('Essa é sua lista de contatos: {}'.format(lista_contatos))
   
    print('Satisfeito por sua resposta')
    agenda = input('Deseja modificar novamente a sua agenda: ').strip().lower()



