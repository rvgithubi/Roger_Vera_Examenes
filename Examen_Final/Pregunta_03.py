""" El decorador retornará la cantidad de parámetros que hayas usado en la 
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta 
lógica, caso contrario indicarlo con un mensaje respectivamente. - Al final de la función decorada indicará mediante un mensaje que la función 
fue ejecutada. - La función que vas a crear va a capturar, la edad, nombre de un alumnos y la  
hora y el minuto en que fue registrado (usar la librería correspondiente de 
tiempo) 
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las 
16 horas con 20 minutos” - La función que será decorada también estará pasando 4 notas que calculará 
la media del estudiante. """""

from datetime import datetime


def decorador_especial(funcion_original):
    def envoltura(*args, **kwargs):

        cantidad_datos = len(args) + len(kwargs)


        resultado = funcion_original(*args, **kwargs)



        return resultado

    return envoltura


@decorador_especial
def registrar_estudiante(nombre, edad, nota1, nota2, nota3, nota4):
    # Hora actual
    ahora = datetime.now()
    hora = ahora.hour
    minutos = ahora.minute


    promedio = (nota1 + nota2 + nota3 + nota4) / 4

    print(" Para {} de {} años fue registrado a las {} horas con {} minutos". format(nombre,edad, hora , minutos))
    print("Sus notas son :", nota1, nota2, nota3, nota4)
    print(" Su promedio es: ", promedio)




estudiante1 = registrar_estudiante("Pedro", 10, 15, 18, 14, 16)