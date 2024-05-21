import random

def adivina_numero():

    numero_secreto = random.randint(1, 10)
    
    intentos = 0
    while True:
        intento = int(input("Adivina el número (entre 1 y 10): "))
        intentos += 1
        
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break

adivina_numero()
