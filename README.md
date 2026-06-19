# Juego del Ahorcado - Python

Este es un pequeño juego del ahorcado hecho en Python donde el jugador debe adivinar el nombre de un videojuego letra por letra.

---

¿Cómo funciona?

El programa elige aleatoriamente un videojuego de una lista y lo oculta usando guiones bajos (`_`).  
El jugador debe ingresar letras hasta adivinar la palabra completa o quedarse sin intentos.

---

## Lógica del juego

- Se selecciona una palabra aleatoria desde una lista (`repertorio`)
- Se reemplazan las letras por `_`
- El jugador introduce letras una por una
- Si la letra está en la palabra, se revela
- Si no está, se pierde un intento
- El jugador gana si adivina toda la palabra antes de quedarse sin intentos

---

##  Lista de juegos incluidos

- Minecraft  
- Nioh  
- Sekiro  
- Bloodborne  
- Red Dead Redemption  
- Dark Souls  
- Cuphead  
- Hollow Knight  
- God of War  
- Elden Ring  

---

##  Requisitos

- Python 3.x

No se necesitan librerías externas, solo módulos estándar:
- `os`
- `random`

---

##  Cómo ejecutar el juego

1. Clona este repositorio:
```bash
git clone https://github.com/kendallsalgado64-max/tarea-ahorcado-.git
