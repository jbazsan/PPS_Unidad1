def binario_decimal(strbinario):
    num_decimal = 0

    for posicion, digito in enumerate(strbinario[::-1]):
        num_decimal += int(digito) * 2 ** posicion

    print(f"La conversión del numero binario: {strbinario} es: {num_decimal}")
    return num_decimal

def esBinario(strbinario):
    for numeros in strbinario:
        if((numeros == "0") or (numeros == "1")):
            print("El número introducido es binario.")

            binario_decimal(strbinario)
            return True
        else:
            print ("El número introducido no es binario.")
            return False
        
unidad = input("Introduce un numero binario: ")
esBinario(unidad)