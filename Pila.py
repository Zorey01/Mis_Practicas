pila = []

for i in range(1, 11):
    pila.append(i)
    print("Apilación de la pila:", pila)
    print("Cima de la pila:", pila[-1])

print("Tamaño de la pila:", len(pila))
print(f"¿La pila está vacía? {len(pila) == 0}")

print("Vaciar la pila")
while pila:
    retirado = pila.pop()
    print("Elemento retirado:", retirado)
    print("Estado de la pila:", pila)
    print(f"¿Está vacía ahora? {len(pila) == 0}")