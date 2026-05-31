jogar = input('Quer testar agora? ').strip().lower()
while jogar == 'sim':
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    
    for n in range (num1, num2+1):
        cont = 0
        for i in range (1, n+1):
            if n % i == 0:
                cont += 1
        if cont == 2:
            print(i, end = ' ')
    print()
    jogar = input('Quer testar novamente? ').strip().lower()

while jogar == 'não':
    num1 = int(input('Digite um número: '))
    cont = 0
    for i in range (1,num1+1):
        if num1 % i == 0:
            cont +=1
    if cont == 2:
        print('O {} é um número primo'.format(num1))
    else: 
        print('O {} não é um número primo'.format(num1))

