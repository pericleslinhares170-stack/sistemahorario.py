from random import randint
lista_temperatura = []
for i in range (6):
    temperatura = randint(150,450)/10
    lista_temperatura.append(temperatura)

print(lista_temperatura)

print()

lista_temperatura.reverse()
print(lista_temperatura)

print()

lista_temperatura.sort()
print(lista_temperatura)

print()

lista_temperatura.sort(reverse=True)
print(lista_temperatura)
