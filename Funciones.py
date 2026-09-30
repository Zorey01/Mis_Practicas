import datetime
def Saludar():
    print("Hola Bienvenid@s")
Saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es : {hora_actual}")
mostrar_hora()

def caclular_area_triangulo(base,altura):
    area = (base*altura)/2
    return  area
resultado=caclular_area_triangulo(150,25)
print(f"El area del triangulo es :{resultado}")

def saludar_persona(nombre,edad):
    print(f"Hola {nombre}, tienes {edad} años")
    saludar_persona ("Edmundo", 19)
    