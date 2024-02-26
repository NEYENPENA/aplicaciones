"""
1 preguntar al usuario su nombre
y contestarle algo como bueno [nombre] he pensado un numnero entre el 1 y el 100 y tines solo 8 intentos para
adivinarlo, cual crees que es el numero.
en cada intento el jugador dara un numero y el programa dira 4 cosas diferentes
a: si el numero es menor a 1 o superior a 100: que a elegido un numero que no esta permitido
b si el numero es menor al que pensado el programa le va a decir que la respuesta es incorrecta y que ha
elegido un numero menor al numnero secreto
c si es mayor lo mismo
d si eligio el numero correcto se le informa que gano y la cantidad de intentos que le llevo
2
si el  usuario no gano se le va a pedir que intente con otro numero hasta que gane o se le acaben los intentos
"""
from random import randint
nombre = input("Hola, ¿cual es tu nombre?\n")
print(f"Bueno {nombre} he pensado un numero entre el 1 y el 100 y tienes solo 6 intentos para adivinarlo. ¿cual"
      f" crees que sea?")
numero_random = randint(1,100)
intentos = 6
veces = 0
while intentos > 0:
    numero_usuario = int(input("Por favor ingresa un numero a continuacion: "))
    intentos -=1
    veces +=1
    if numero_usuario < numero_random and intentos > 0 :
        print("la respuesta es incorrecta, elegiste un numero menor al numero secreto. Vuelve a intentarlo ")
        print(f"te quedan {intentos} intentos")
    elif numero_usuario > numero_random and intentos > 0 :
        print("La respuesta es incorrecta, elegiste un numero mayor al numero secreto. Vuelve a intentarlo")
        print(f"te quedan {intentos} intentos")
    elif numero_usuario < 1 or numero_usuario > 100 and intentos > 0:
        print("elegiste un numero fuera del rango permitido")
        print(f"te quedan {intentos} intentos")
    elif numero_usuario == numero_random:
        print(f"¡Felicitaciones {nombre}! el numero secreto es {numero_random} y lo conseguiste en solo {veces} intentos")
        break

if intentos == 0 and numero_random != numero_usuario:
        print(f"Lo siento no tienes mas intentos, El numero secreto era {numero_random}\nGame Over")