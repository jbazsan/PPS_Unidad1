def estaEnRango(valor, min, max):
    if valor > max:
        print("Has introducido un numero mayor al intervalo especificado anteriormente.")
        return False
    elif valor < min:
        print("Has introducido un numero menor al intervalo especificado anteriormente.")
        return False
    else:
        print("Has introducido un numero adecuado al intervalo especificado anteriormente.")
        return True

def estaEnLista(valor, lista):

    find = 0

    for valores in lista:
        if valor == valores:
            find = 1
    if find == 1:
        print("El numero está en lista")
        return True
    else:
        print("El numero no esta en lista")
        return False
    
valor = int(input("Introduzca un numero entre 1 y 20: "))
min = 1
max = 20

estaEnRango(valor, min, max)

lista = [5, 14, 11, 3, 2, 1, 15, 19]

valor = int(input("Introduzca el numero de nuevo: "))
estaEnLista(valor, lista)