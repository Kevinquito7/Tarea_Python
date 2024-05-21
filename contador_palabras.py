def contar(cadena):

    palabras = cadena.split()
  
    num_palabras = len(palabras)
    return num_palabras

texto = input("Introduce un texto: ")
num_palabras = contar(texto)
print(f"El número de palabras en la cadena es: {num_palabras}")