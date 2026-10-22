from collections import deque
import time
cola_reproduccion = deque()
#Agregar elementos de reproducción
cola_reproduccion.append("1.- Mochila Azul")
cola_reproduccion.append("2.- Aerolinea Carrillo")
cola_reproduccion.append("3.- La calabaza")
#Mostrar las canciones en espera
print("Canción en espera:")
for cancion in cola_reproduccion:
    print("_", cancion)
    print("Iniciando Reproducción:")
#Desencolar
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"Sonando ahora: {cancion_actual}")
    time.sleep(1)  # Simula la duración de la canción
print(f"Finalizo {cancion_actual}")
#Muestra cauntas canciones quedan en la cola
print(f"Quedan {len(cola_reproduccion)} canciones en la cola")
print("La cola de reproducción ha finalizado")