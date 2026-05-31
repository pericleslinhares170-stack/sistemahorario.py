from colorama import Fore,Back,init
opcao = ''
init(autoreset=True)
while opcao != 0:
    print(Fore.BLACK + Back.GREEN+ """                                                            --------------------------------------------------------                                                                                                                          
                                                            |      PROJETO DE GESTÃO DE HORÁRIOS DE UMA ESCOLA      |                                                                                           
            
                                                            --------------------------------------------------------                                                                                      """)
    print(Fore.BLACK + Back.GREEN+'                                                                                                                                                                        ')
    print(Fore.BLACK + Back.GREEN+ '                                                          | 1- Portal Do Professor                            |                                                        ')
    print(Fore.BLACK + Back.GREEN+ '                                                          | 2- Portal Do Aluno                                |                                                        ')
    print(Fore.BLACK + Back.GREEN+ '                                                          | 3- Relatório Sobre Os Horários Das Aulas          |                                                        ')
    print(Fore.BLACK + Back.GREEN+ '                                                          | 0- Sair Do Sistema                                |                                                        ')
    print(Fore.BLACK + Back.GREEN+'                                                                                                                                                                        ')
    opcao = int(input(Fore.WHITE + '                                                            Digite a opção que deseja acessar: '       
                                                                ))
    print()
    if opcao == 1:
        print(Fore.BLACK+Back.GREEN+'                                                                    --------------------------------------------------------                                                                 ')
        print(Fore.BLACK+Back.GREEN+'                                                                    |  1- Cadastro De Aulas                                |                                                                 ')
        print(Fore.BLACK+Back.GREEN+'                                                                    |  2- Exclusão De Horários                             |                                                                 ')
        print(Fore.BLACK+Back.GREEN+'                                                                    |  3- Verifiicação De Horários                         |                                                                 ')
        print(Fore.BLACK+Back.GREEN+'                                                                    --------------------------------------------------------                                                                 ')
        opcao2 = int(input('                                                                             Digite a opção que deseja acessar: '))
        if opcao2 == 1:
            print(Fore.BLACK+Back.GREEN+'                                                                ------------------------------------------------------------                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |                                                          |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |              MÓDULO EM DESENVOLVIMENTO...                |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |                                                          |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                ------------------------------------------------------------                                                                 ')
            input('                                                                                      APERTE >ENTER< PARA PULAR                                                                                                         ')    
        elif opcao2 == 2:
            print(Fore.BLACK+Back.GREEN+'                                                                ------------------------------------------------------------                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |                                                          |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |              MÓDULO EM DESENVOLVIMENTO...                |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |                                                          |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                ------------------------------------------------------------                                                                 ')
            input('                                                                                      APERTE >ENTER< PARA PULAR                                                                                                          ')
        elif opcao2 == 3:
            print(Fore.BLACK+Back.GREEN+'                                                                ------------------------------------------------------------                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |                                                          |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |              MÓDULO EM DESENVOLVIMENTO...                |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |                                                          |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                ------------------------------------------------------------                                                                 ')
            input('                                                                                      APERTE >ENTER< PARA PULAR                                                                                                         ')
        else:
            print(Fore.BLACK+Back.GREEN+'                                                                ------------------------------------------------------------                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |                                                          |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |                     OPÇÃO INEXISTENTE                    |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                |                                                          |                                                                 ')
            print(Fore.BLACK+Back.GREEN+'                                                                ------------------------------------------------------------                                                                 ')
            input('                                                                                      APERTE >ENTER< PARA PULAR                                                                                                         ')
    elif opcao == 2:
        print(Fore.BLACK+Back.GREEN+'                                                                    --------------------------------------------------------                                                                 ')
        print(Fore.BLACK+Back.GREEN+'                                                                    |  1- Cadastro De Aulas                                |                                                                 ')
        print(Fore.BLACK+Back.GREEN+'                                                                    |  2- Exclusão De Horários                             |                                                                 ')
        print(Fore.BLACK+Back.GREEN+'                                                                    |  3- Verifiicação De Horários                         |                                                                 ')
        print(Fore.BLACK+Back.GREEN+'                                                                    --------------------------------------------------------                                                                 ')