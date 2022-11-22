from random import choice, sample

print("Vamos a jugar al Black Jack")


cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}
print("Cartas: {}".format(" ".join(cartas.keys())))
print("Puntos: {}".format(list(cartas.values())))

print("Cada carta tiene su valor")
print("Mira")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

lista_cartas = list(cartas)

print(" ")

print("Escoge dos cartas")
print("Has escogido:   ", end=" ")
carta = choice(lista_cartas)
score = cartas[carta]
print(carta, end=" ")
carta = choice(lista_cartas)
score += cartas[carta]
print(carta, end=" ")
print("Tu puntuación es: ", score)

print(" ")

print("Ahora tu rival va a escoger 2 cartas")
print("Tu rival tiene: ", end=" ")
carta = choice(lista_cartas)
score_rival = cartas[carta]
print(carta, end=" ")
carta = choice(lista_cartas)
score_rival += cartas[carta]
print(carta, end=" ")
print("Su puntuación es: ", score_rival)

print(" ")

def menu():
    if score >= score_rival:
        print("Ganaste")
    elif score <= score_rival:
        print("Perdiste")
    else:
        print("Empate")

menu()