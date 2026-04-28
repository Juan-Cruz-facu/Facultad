def romano_a_decimal(romano):
    """
    Convierte un número romano (string) a un número decimal (entero).
    """
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    prev_valor = 0
    
    # Recorremos el número romano de derecha a izquierda
    for letra in reversed(romano.upper()):
        valor = valores[letra]
        # Si el valor actual es mayor o igual al anterior, se suma (ej. VI -> suma 1 y suma 5)
        # Si es menor, se resta (ej. IV -> suma 5 y resta 1)
        if valor >= prev_valor:
            decimal += valor
        else:
            decimal -= valor
        prev_valor = valor
        
    return decimal

# Ejemplos de prueba
if __name__ == "__main__":
    print(f"IX en decimal es: {romano_a_decimal('IX')}")       # 9
    print(f"XIV en decimal es: {romano_a_decimal('XIV')}")     # 14
    print(f"MCMXCIV en decimal es: {romano_a_decimal('MCMXCIV')}") # 1994
