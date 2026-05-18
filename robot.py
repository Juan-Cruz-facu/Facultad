def registrar_movimiento(historial, direccion, pasos):
    historial.append({"direccion": direccion.lower(), "pasos": pasos})

def generar_regreso(historial_ida):
    opuestos = {
        "norte": "sur", "sur": "norte",
        "este": "oeste", "oeste": "este",
        "noreste": "suroeste", "suroeste": "noreste",
        "noroeste": "sureste", "sureste": "noroeste"
    }
    
    camino_regreso = []
    
    # Se recorre el historial al revés (comportamiento LIFO) para volver
    for movimiento in reversed(historial_ida):
        direccion_ida = movimiento["direccion"]
        pasos = movimiento["pasos"]
        
        direccion_vuelta = opuestos[direccion_ida]
        camino_regreso.append({"direccion": direccion_vuelta, "pasos": pasos})
        
    return camino_regreso

# --- Bloque de Prueba ---
if __name__ == "__main__":
    historial_robot = []
    registrar_movimiento(historial_robot, "norte", 5)
    registrar_movimiento(historial_robot, "noreste", 3)
    registrar_movimiento(historial_robot, "este", 10)

    for mov in generar_regreso(historial_robot):
        print(f"Regreso: {mov['pasos']} pasos hacia el {mov['direccion']}")
