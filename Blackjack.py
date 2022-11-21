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

print("Mira las cartas")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

print("Toma estas dos cartas")
lista_cartas = list(cartas)

print("Ha seleccionado:", end=" ")
carta = choice(lista_cartas)
score = cartas[carta]
print(carta, end=" ")
carta = choice(lista_cartas)
score += cartas[carta]
print(carta, end=" ")
print(" tu puntuación es de:", score)


main_banca = sample(lista_cartas, 2)
score_banca = sum(cartas[carta] for carta in main_banca)
print("La banca tiene: {} {} la banca ha sacado: {}".format(main_banca[0],
                                                          main_banca[1],
                                                          score_banca))