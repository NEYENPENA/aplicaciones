"""
pedir al usuario que ingrese un texto (ej: Poesia)
luego el pedir al usuario que ingrese 3 letras cualquiera

1cuantas veces aparecen en el texto cada una de las letras q ingreso el usuario
almacenar las letras en una lista
usar un metodo de string q nos permita contar cuantas veces aparece
pasar todo a minuscula texto y letras
2 decirle al usuario cuantas palabras hay a lo largo detodo el texto
usar el metodo que permite pasar todo a lista y luego funcion len para ver
el largo
3 cual es la primera y cual es la ultima letra usar indexado
4 mostrar como queda el texto si invertimos el orden de las palabras
usar metodo q invierte el orden de una lista
5 decir si la palabra python aparece en el texto
usar booleanos  y diccionario para expresar la respuesta
"""
textoUsuario = input("Introduce un texto: ")
textoUsuario = textoUsuario.lower()
#creo una lista vacia
letrasUsuario = []
#almaceno las letras en las lista usando la funcion append
# paso a minusculas utilizando el metodod de str lower ya que es un string lo que ingresa el usuario
letrasUsuario.append(input("Introduce la primera letra: ").lower())
letrasUsuario.append(input("Introduce la segunda letra: ").lower())
letrasUsuario.append(input("Introduce la tercera letra: ").lower())
print("\n")
print("CANTIDAD DE LETRAS")
#creo 3 variables para almacenar cada letra que aparezca en el texto utilizando el metodo count
# que retorna el numero de veces q se repite la letra y la almacena en la variable
cantidad_Letras1 = textoUsuario.count(letrasUsuario[0])
cantidad_Letras2 = textoUsuario.count(letrasUsuario[1])
cantidad_Letras3 = textoUsuario.count(letrasUsuario[2])

print(f"la letra '{letrasUsuario[0]}' aparece {cantidad_Letras1} veces")
print(f"la letra '{letrasUsuario[1]}' aparece {cantidad_Letras2} veces")
print(f"la letra '{letrasUsuario[2]}' aparece {cantidad_Letras3} veces")

#Al texto almacenado en la varible lo separo y almaceno en una lista usando el metodo split
#Que guarda cada elemento [las palabras] separado por un espacio)
#luego utilizo la funcion len para contar todos los elementos de la lista
print("\n")
print("CANTIDAD DE PALABRAS")
palabras_Lista = textoUsuario.split()
cantidad_Palabras = len(palabras_Lista)
print(f"El texto ingresado tiene {cantidad_Palabras} palabras en total")
print("\n")
print("LETRAS DE INICIO Y FIN")

#accedo a los elementos de la lista a travez de su indice y los almaceno en variables
primer_letra = textoUsuario[0]
ultima_Letra = textoUsuario[-1]
print(f"la primer letra del texto es: '{primer_letra}'")
print(f"la ultima letra del texto es: '{ultima_Letra}'")

print("\n")
print("TEXTO INVERTIDO")
#utilizando la lista ya creada la invierto
#Utilizo el metodo join para unir la lista de palabras usando un espacio
palabras_Lista.reverse()
texto_invertido = " ".join(palabras_Lista)
print(f"Este es tu texto invertido: '{texto_invertido}'")

print("\n")
print("¿LA PALABRA PYTHON APARECE EN EL TEXTO?")

buscar_Python = "python" in palabras_Lista
dic = {True: "Si", False: "No"}
print(f"La palabra 'python' {dic[buscar_Python]} aparece en el texto")