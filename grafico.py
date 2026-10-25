import matplotlib.pyplot as plt

datos = [42, 12, 89, 25, 8, 66, 37, 50]

# ALGORITMO DE INSERCIÓN
def insercion(arr):
    a = arr.copy()
    comp = 0
    for i in range(1, len(a)):
        clave, j =a[i], i - 1
        while j >= 0 and a[j] > clave:
            comp +=1
            a[j + 1] = a[j]
            j -= 1
            if j>=0: comp +=1
            a[j + 1] = clave
    return a, comp

# ALGORITMO DE SELECCIÓN

def seleccion(arr):
    a = arr.copy()
    comp = 0
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp +=1
            if a[j] < a[min_idx]:
                min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i]
    return a, comp

# 2. Ejecución de ambos algoritmos
lista_ordenada, comp_isn = insercion(datos)
_, comp_sel = seleccion(datos)

# 3. Graficación
fig, (ax1, ax2, ax3) = plt.subplots(1, 2, figsize=(12, 5))