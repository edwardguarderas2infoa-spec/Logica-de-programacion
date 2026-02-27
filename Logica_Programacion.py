
import random

OPCIONES = ["piedra", "papel", "tijera"]

def mostrar_menu():
    print(" Elige una opcion Piedra, Papel o Tijera ")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")

def eleccion_jugador():
    while True:
        try:
            opcion = int(input("Elige una opción (1-4): "))
            if opcion == 4:
                return "Salir"
            elif opcion in [1,2,3]:
                return OPCIO
                OPCIONES[opcion - 1]
            else:
                print("Opción inválida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


def eleccion_computadora():
    return random.choice(OPCIONES)


def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "jugador"
    else:
        return "computadora"

