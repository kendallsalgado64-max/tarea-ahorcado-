import os
import random

repertorio = ["minecraft", "nioh", "sekiro", "bloodborne","red dead redemption", "dark souls", "cuphead","hollow knight", "god of war", "elden ring"]

juego = random.choice(repertorio)  # permite escoger una palabra random de la lista
separada = list(juego)
print(separada)
adivinar = []

for caracter in separada:
    if caracter == " ":
        adivinar.append(" ")
    else:
        adivinar.append("_")

while "_" in adivinar:

    print("\n" + " ".join(adivinar))  # pone un espacio vacio antes de cada letra
    letra = input("Introduce una letra: ").strip().lower()#entrada de usuario baja todo a minusculas
    for i, caracter in enumerate(separada):  # recorre cada elemento de la lista
        if caracter == letra:  # evalua iguales entre lista y entrada
            adivinar[i] = letra  # reemplaza los guiones por letras

print("¡Has ganado!")
print("La palabra era:", juego)