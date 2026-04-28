def usar_la_fuerza(mochila, objetos_sacados=0):
    """
    Busca un 'sable de luz' en la mochila de forma recursiva.
    Sacará objetos de la mochila de a uno hasta encontrarlo o vaciar la mochila.
    Devuelve una tupla: (booleano_encontrado, cantidad_de_objetos_sacados)
    """
    # Condición base 1: no quedan más objetos en la mochila
    if len(mochila) == 0:
        return False, objetos_sacados
    
    # Extraemos el primer objeto que tenemos a mano en la mochila
    objeto_actual = mochila.pop(0)
    objetos_sacados += 1
    
    # Condición base 2: encontramos el sable de luz
    if objeto_actual == "sable de luz":
        return True, objetos_sacados
    
    # Llamada recursiva con el resto de la mochila (ya sin el objeto que sacamos)
    return usar_la_fuerza(mochila, objetos_sacados)

# Ejemplos de prueba
if __name__ == "__main__":
    # Caso 1: Tiene el sable
    mochila_jedi = ["comida", "botiquín", "comunicador", "sable de luz", "capa"]
    print(f"Mochila inicial: {mochila_jedi}")
    
    encontrado, cantidad = usar_la_fuerza(mochila_jedi)
    
    if encontrado:
        print(f"¡El Jedi sobrevivió! Encontró el sable de luz después de sacar {cantidad} objetos.")
    else:
        print(f"No encontró el sable de luz tras sacar {cantidad} objetos.")
        
    print("-" * 40)
    
    # Caso 2: No tiene el sable
    mochila_jedi_2 = ["comida", "botiquín", "agua"]
    print(f"Mochila inicial: {mochila_jedi_2}")
    
    encontrado, cantidad = usar_la_fuerza(mochila_jedi_2)
    
    if encontrado:
        print(f"¡El Jedi sobrevivió! Encontró el sable de luz después de sacar {cantidad} objetos.")
    else:
        print(f"Murió :( No encontró el sable de luz tras vaciar la mochila (sacó {cantidad} objetos).")
