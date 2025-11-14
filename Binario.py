def decimal_a_binario(n):
    """Convierte un número decimal a binario."""
    if n == 0:
        return "0"
    binario = ""
    pasos = []  # Guardamos los pasos para mostrar al usuario
    while n > 0:
        resto = n % 2
        pasos.append(f"{n} / 2 = {n // 2} (resto {resto})")
        binario = str(resto) + binario
        n = n // 2
    print("\n--- Proceso paso a paso ---")
    for p in pasos:
        print(p)
    return binario

def binario_a_decimal(b):
    """Convierte un número binario (como cadena) a decimal."""
    decimal = 0
    potencia = 0
    pasos = []
    for digito in reversed(b):
        valor = int(digito) * (2 ** potencia)
        pasos.append(f"{digito} × 2^{potencia} = {valor}")
        decimal += valor
        potencia += 1
    print("\n--- Proceso paso a paso ---")
    for p in pasos:
        print(p)
    return decimal

# Programa principal
print("=== Conversor Binario ↔ Decimal ===")

while True:
    print("\n¿Qué querés hacer?")
    print("1. Convertir de Decimal a Binario")
    print("2. Convertir de Binario a Decimal")
    print("3. Salir")

    opcion = input("Elegí una opción (1, 2 o 3): ")

    if opcion == "1":
        try:
            numero_decimal = int(input("Ingresá un número decimal: "))
            numero_binario = decimal_a_binario(numero_decimal)
            print(f"\nEl número decimal {numero_decimal} en binario es {numero_binario}")
        except ValueError:
            print("Por favor, ingresá un número entero válido.")
    
    elif opcion == "2":
        numero_binario = input("Ingresá un número binario (solo 0 y 1): ")
        if all(d in "01" for d in numero_binario):
            numero_decimal = binario_a_decimal(numero_binario)
            print(f"\nEl número binario {numero_binario} en decimal es {numero_decimal}")
        else:
            print("El número ingresado no es un binario válido.")
    
    elif opcion == "3":
        print("Fin del programa.")
        break
    else:
        print("Opción inválida. Elegí 1, 2 o 3.")



