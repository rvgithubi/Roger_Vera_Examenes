
from datetime import datetime

def decorador_hora(func):
    def funcionA(*args, **kwargs):

        ahora = datetime.now()

        print("Decorador está siendo ejecutado a las {} horas con {} minutos".format(ahora.hour, ahora.minute))
        resultado = func(*args, **kwargs)

        return resultado
    return funcionA

@decorador_hora
def encontrar_mayor(**numeros):
    mayor = max(numeros.values())
    print("De los números {}, el mayor es: {}".format(numeros, mayor))
    return mayor



encontrar_mayor(a=5, b=10, c=3, d=8, e=1, f=7)