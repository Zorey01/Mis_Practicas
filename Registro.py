def mostrar_encabezado_escuela():
    print("Universidad Técnologica de Xicotepec de Juarez")
    print("Reporte de Calificaciones")
mostrar_encabezado_escuela()

print("\n---------------------------\n")

def obtener_nota_minima_aprobatoria():
    return 6.0

nota_minima = obtener_nota_minima_aprobatoria()
print(f"La nota mínima necesaria para aprobar es: {nota_minima}")
print("\n---------------------------\n")

def evalua_rendimiento(nota_final):
    if nota_final <7.0:
        return "Reprobado"
    elif 7.0 <= nota_final <=9.4:
        return "Aprobado"
    elif 9.5 <= nota_final <=10.0:
        return "Excelente"
    else:
        return "Lo siento, esta fuera de rango."
print("\n---------------------------\n")

est1 = evalua_rendimiento(9.8)
print(f"Rendimiento con nota 9.8: {est1}")
est2 = evalua_rendimiento(6.5)
print(f"Rendimiento con nota 6.5: {est2}")

print("\n---------------------------\n")

def cal_prom_pond (nota_ex, nota_tare):
    prom = (nota_ex * 0.70) + (nota_tare * 0.30)
    return round(prom, 1)
prom_final = cal_prom_pond(9.5, 8.0)
print(f"El promedio ponderado final es: {prom_final}")

print("\n---------------------------\n")

def gen_bol(nom_alum, not_ex, not_tare):
    mostrar_encabezado_escuela

    not_final = cal_prom_pond(not_ex, not_tare)
    not_mini = obtener_nota_minima_aprobatoria()
    estado = evalua_rendimiento(not_final)

    print(f"Alumno: {nom_alum}")
    print(f"Nota Final: {not_final}")
    print(f"Estado Académico: {estado}")

    if  not_final < not_mini:
        print("Aviso: Requiere presentar examen extraordinario")
    else:
        print("Aviso: No requiere examen extraordianrio")

gen_bol("Edmundo", 8.5, 9.0)
print()
gen_bol("Hugo", 5.0, 6.5)