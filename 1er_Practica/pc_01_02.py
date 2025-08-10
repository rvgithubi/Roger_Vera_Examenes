"""
Se tiene un alumno con calificaciones en tres cursos:
Matemáticas: 17, Ciencia: 14, Historia: 15
Cada curso tiene un peso diferente en la nota final:
Matemáticas: 40%, Ciencia: 30%, Historia: 30%
Realizar lo que se pide a continuación:
Calcula la nota final ponderada del alumno.
Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal.
Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano:
"¿Aprobado?: True" o "¿Aprobado?: Sí"
Genera una cadena resumen que diga:
"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado"
En caso no apruebe indicar lo contrario en los mensajes

"""

# Calificaciones y pesos
matematicas = 17
ciencia = 14
historia = 15

peso_matematicas = 0.40
peso_ciencia = 0.30
peso_historia = 0.30

# Cálculo de la nota final ponderada
nota_final = (matematicas * peso_matematicas) + (ciencia * peso_ciencia) + (historia * peso_historia)
aprobado = nota_final >= 13.0
if aprobado:
    print("¿Aprobado?: SI" )
    estado = "Aprobado"
else:
    print("¿Aprobado?: NO")
    estado = "Reprobado"

# Mostrar la nota final con 1 decimal
print("La nota final es " , format(nota_final, '.1f'))

# Generar cadena resumen
print("El estudiante obtuvo una nota final de {}  y su estado final es {} ". format(format(nota_final, '.1f'),estado))
