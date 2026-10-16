historial_navegacion=[]
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.org")

print("historial cargando", historial_navegacion)
#Operación cima(Top/Peek)

pagina_actual=historial_navegacion[-1]
print("Pagina actual en pantalla;", pagina_actual)

#Operación de desapiilar(Pop)
pagina_cerrada=historial_navegacion.pop()
print("Saliendo de",pagina_cerrada)
print("Historial despues de presionar 'Atras':", historial_navegacion)

#Tamaño de las pilas
total_paginas=len(historial_navegacion)
print("Páginas guardadas:", total_paginas)

#Operación vacia(Empty)
sin_paginas=len(historial_navegacion)==0
print("¿El historial esta vacio?", sin_paginas)
