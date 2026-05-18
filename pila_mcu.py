# Operaciones abstractas de Pila
def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    return pila.pop() if pila else None

def pila_vacia(pila):
    return len(pila) == 0

def analizar_pila_mcu(pila_mcu):
    pila_auxiliar = []
    posicion_actual = 1
    
    pos_rocket = -1
    pos_groot = -1
    personajes_mas_de_5 = []
    pelis_viuda_negra = 0
    empiezan_con_cdg = []

    # Desapilamos hacia una auxiliar para no perder los datos originales
    while not pila_vacia(pila_mcu):
        personaje = desapilar(pila_mcu)
        nombre = personaje["nombre"]
        pelis = personaje["peliculas"]
        
        if nombre == "Rocket Raccoon":
            pos_rocket = posicion_actual
        elif nombre == "Groot":
            pos_groot = posicion_actual
            
        if pelis > 5:
            personajes_mas_de_5.append((nombre, pelis))
            
        if nombre in ["Black Widow", "Viuda Negra"]:
            pelis_viuda_negra = pelis
            
        if nombre[0].upper() in ['C', 'D', 'G']:
            empiezan_con_cdg.append(nombre)
            
        apilar(pila_auxiliar, personaje)
        posicion_actual += 1

    # Restauramos la pila original
    while not pila_vacia(pila_auxiliar):
        apilar(pila_mcu, desapilar(pila_auxiliar))

    print(f"a. Posición Rocket: {pos_rocket} | Posición Groot: {pos_groot}")
    print(f"b. Más de 5 películas: {personajes_mas_de_5}")
    print(f"c. Películas de Viuda Negra: {pelis_viuda_negra}")
    print(f"d. Empiezan con C, D o G: {empiezan_con_cdg}")

# --- Bloque de Prueba ---
if __name__ == "__main__":
    pila_personajes = [
        {"nombre": "Captain America", "peliculas": 7},
        {"nombre": "Black Widow", "peliculas": 8},
        {"nombre": "Groot", "peliculas": 4},
        {"nombre": "Doctor Strange", "peliculas": 4},
        {"nombre": "Rocket Raccoon", "peliculas": 4} # Cima de la pila (posición 1)
    ]
    
    analizar_pila_mcu(pila_personajes)
