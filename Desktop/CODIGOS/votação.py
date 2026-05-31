lista_temperaturas = []
temperatura_acima = 0
lista_acima = []
for i in range (8):
    temperatura = float(input(f'Digite a {i+1}° temperatura do paciente: '))
    lista_temperaturas.append(temperatura)

media = sum(lista_temperaturas) / len(lista_temperaturas)
print('Essa é a média das temperaturas: {}'.format(media))

for temperatura in lista_temperaturas:
    if temperatura > media:
        temperatura_acima += 1
        lista_acima.append(temperatura)
print(f'O paciente ficou com a temperatura acima da média por {temperatura_acima}')
print(lista_acima)