"""- Crear una función que le permitirá almacenar X números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función. X solo
puede ser entero. No otro tipo de dato. Y también un índice existente en la
lista. - Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola. - Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.  - Crear una función para indicar cuál es el mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola. - Crear el archivo principal.py, donde solo llamarás las anteriores funciones
que se encontrarán alojadas en un módulo"""

def generar_numeros_aleatorios():
    while True:
        try:
            x = int(input("Ingrese la cantidad de números aleatorios a generar: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero")

    numero = []
    for num in range(x):

        valor= int(input("Ingrese numeros aleatorios: "))
        numero.append(valor)


    print("\nLista original generada:")
    for num in numero:
        print("los numeros son: ",num )
    return numero


def obtener_no_repetidos(lista_original):

    no_repetidos = list(set(lista_original))
    print("\nNúmeros no repetidos:")
    print(no_repetidos)
    return no_repetidos


def ordenar_listas(lista):
    mayor_a_menor = sorted(lista, reverse=True)
    menor_a_mayor = sorted(lista)

    print("\nLista ordenada de mayor a menor:")
    print(mayor_a_menor)
    print("\nLista ordenada de menor a mayor:")
    print(menor_a_mayor)

    return mayor_a_menor, menor_a_mayor


def mayor_numero_par(lista):

    pares = [num for num in lista if num % 2 == 0]

    if not pares:
        print("\nNo hay números pares en la lista")
        return None

    mayor_par = max(pares)
    print(f"\nEl mayor número par es: {mayor_par}")
    return mayor_par