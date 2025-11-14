print("=== Operaciones con Conjuntos ===")

# Pedimos dos listas separadas por comas
grupo1 = input("Ingresá los elementos del primer grupo separados por comas: ")
grupo2 = input("Ingresá los elementos del segundo grupo separados por comas: ")

# Convertimos las cadenas en conjuntos
A = set(grupo1.replace(" ", "").split(","))
B = set(grupo2.replace(" ", "").split(","))

# Mostramos las operaciones
print("\nUnión:", A | B)
print("Intersección:", A & B)
print("Diferencia (A - B):", A - B)