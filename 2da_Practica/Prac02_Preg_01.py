"""1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiantes.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio"""


estudiante = { "roger":[20,19,20], "carlos":[19,17,12], "fedri": [21,22,23]}


#print(estudiante.items())
def procesar_notas(estudiante):
    final = {}
    mayorprom = 0
    mejorestudiante = "null"

    #final = estudiante.keys()
    for nombre, notas in estudiante.items():
        promedio = round(sum(notas)/len(notas),2)
        if promedio > mayorprom:
            mayorprom = promedio
            mejorestudiante = nombre

        if promedio >= 11:
            estado = "Aprobado"
        else:
            estado = "Desaprobado"
      # print(f"{nombre} El promedio  es: {promedio}")
        final[nombre] = {"promedio":promedio, "estado":estado}
    print("Mejor estuadiante: ",nombre)
    return final



print(procesar_notas(estudiante))





