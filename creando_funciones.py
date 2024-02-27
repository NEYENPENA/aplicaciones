# Ejercicio 1; Devolver el numero que corresponde
def devolver_distintos():

    num1 = int(input("Primer Numero "))
    num2 = int(input("Segundo Numero "))
    num3 = int(input("Tercer Numero "))
    lista = [num1, num2, num3]
    total = num1 + num2 + num3
    numero_mayor = max(num1, num2, num3)
    numero_menor = min(num1, num2, num3)
    if total > 15:
            return numero_mayor
    elif total < 10:
        return numero_menor
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos())

# Ejercicio 2; ordenar palabra sin sus letras repetidas
def orden_palabras(palabra):
    palabra_user = []
    for letra in palabra:
        if letra not in palabra_user:
            palabra_user.append(letra)
            palabra_user.sort()
        else: pass
    return palabra_user

print(orden_palabras("entretenido"))
# Ejercicio 3; Comprobar si hay 2 ceros seguidos
def comprobar_ceros(*args):

    contador = 0

    for num in args:

        if args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(comprobar_ceros(5,5,5,6,3,2,1,4,0,1,8,0,7))

# Ejercicio 4; Contar numeros primos
def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2: return 0
    while iteracion <= numero:
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(150))
