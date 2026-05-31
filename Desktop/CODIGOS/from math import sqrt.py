lista_nomes = []
lista_telefone = []
lista_gmail = []
lista_datanascimento = []


quantidade_pessoas = int(input('Digite a quantidade de pessoas que terão os seus dados armazenados: '))
for i in range(quantidade_pessoas):
    nomes = input(f'Digite o nome da {i+1}° pessoa: ').strip()
    lista_nomes.append(nomes)
    telefone = input(f'Digite o telefone da {i+1}° pessoa: ').strip()
    lista_telefone.append(telefone)
    gmail = input(f'Digite o Gmail da {i+1}° pessoa: ').strip()
    lista_gmail.append(gmail)
    data_nascimento = input(f'Digite a data de nascimento da {i+1}° pessoa: ').strip()
    lista_datanascimento.append(data_nascimento)

motivacao = input('Você quer consultar ou armazenar os dados? ').strip()
if motivacao == 'consultar': 
    consulta = input('O que deseja procurar (nome, telefone, gmail ou data de nascimento)? ').strip()
    if consulta == 'nome': 
        nome = input('Digite o nome da pessoa: ').strip()
        if nome in lista_nomes:
            print('Esse nome já está armazenado')
        else: 
            print('Esse nome não está armazenado aqui')
            armazenar = input('Deseja armazenar? ').strip()
            if armazenar == 'sim': 
                nome = input('Digite o nome: ')
                print('Obrigado pela informação!')
            print('Obrigado pela consulta!')