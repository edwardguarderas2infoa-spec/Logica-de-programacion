
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
                return OPCIONES[opcion - 1]
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
def jugar():
    puntos_jugador = 0
    puntos_computadora = 0
    
    print("Bienvenido al juego Piedra, Papel o Tijera")
    
    while True:
        mostrar_menu()
        jugador = eleccion_jugador()
        
        if jugador == "salir":
            break
        
        computadora = eleccion_computadora()
        
        print(f"Tú elegiste: {jugador}")
        print(f"La computadora eligió: {computadora}")
        
        resultado = determinar_ganador(jugador, computadora)
        
        if resultado == "empate":
            print("Resultado: ¡Empate!")
        elif resultado == "jugador":
            print("Resultado: ¡Ganaste la ronda!")
            puntos_jugador += 1
        else:
            print("Resultado: La computadora gana la ronda.")
            puntos_computadora += 1
        
        print(f"Puntaje -> Jugador: {puntos_jugador} | Computadora: {puntos_computadora}")
    
    print("\n=== Juego terminado ===")
    print(f"Puntaje final -> Jugador: {puntos_jugador} | Computadora: {puntos_computadora}")
    
    if puntos_jugador > puntos_computadora:
        print("¡Felicidades! Ganaste el juego.")
    elif puntos_jugador < puntos_computadora:
        print("La computadora ganó el juego.")
    else:
        print("El juego terminó en empate.")

if __name__ == "__main__":
    jugar()