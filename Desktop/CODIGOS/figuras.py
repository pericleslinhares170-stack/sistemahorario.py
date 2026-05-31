from random import randint 

jogar = input('Você quer jogar agora? '.title()).strip().lower()
print()
while jogar == 'sim':
    numero_escolhido = int(input('Digite um número entre 1 e 100: '))
    numero_sorteado = randint(1,100)
    cont = 0
    while numero_escolhido != numero_sorteado: 
        if numero_escolhido > numero_sorteado:
            numero_escolhido = int(input('Digite um número menor: '))
            
            
        elif numero_escolhido < numero_sorteado:
            numero_escolhido = int(input('Digite um número maior: '))
        cont +=1    
            
    print('Parabéns! Você acertou o número')
    
    print()

    if cont < 3:
        print('Você é muito bom!')
    else:
        print('Revise a sua estratégia para a próxima tentativa')

        print()

    jogar = input('Você quer jogar novamente? '.title()).strip().lower()
    print()
print('Obrigado por jogar!'.title())