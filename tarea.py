import os
import random

repertorio = ["minecraft", "nioh", "sekiro", "bloodborne","red dead redemption", "dark souls", "cuphead","hollow knight", "god of war", "elden ring"]

juego = random.choice(repertorio)  # permite escoger una palabra random de la lista
separada = list(juego)

adivinar = []#crea una lista vacia

for caracter in separada:  # recorre todos los elementos de la lista separada
    if caracter == " ":  # detecta los espacios entre palabras
        adivinar.append(" ")  # agrega el espacio directamente
    else:
        adivinar.append("_")  # si es una letra, agrega un "_"

intentos = 5
print("adivina el juego!")
while "_" in adivinar and intentos > 0:# si aun quedan espacios sin adivinar se sigue ejecutando mientras queden intentos
    os.system("cls")
    print("\n" + " ".join(adivinar))  # muestra la palabra oculta
    print("Intentos restantes:", intentos)

    letra = input("Introduce una letra: ").strip().lower()# hace que la entrada del usuario siempre sea minuscula

    encontrada = False#se crea una variable con el boleano falso

    for i, caracter in enumerate(separada):  # recorre cada elemento de la lista
        if caracter == letra:  # evalúa iguales entre lista y entrada
            adivinar[i] = letra  # reemplaza los guiones por letras
            encontrada = True

    if encontrada == False:
        intentos -= 1#si encontrada es  falso se resta uno a la cantidad de intentos restantes
        print("Esa letra no está en la palabra.")

if "_" not in adivinar:# si ya no quedan "_" y aun quedan intentos significa que has ganado
    print("\n¡Has ganado!")
    print("el juego en efecto era:", juego)
else:
    print("\nHas perdido")#sino perdiste
    print("el juego era:", juego)