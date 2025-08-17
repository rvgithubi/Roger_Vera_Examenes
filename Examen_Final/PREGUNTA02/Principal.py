from Pregunta_02 import *



print("INICIO DEL PROGRAMA")


lista_original = generar_numeros_aleatorios()
no_repetidos = obtener_no_repetidos(lista_original)
mayor_menor, menor_mayor = ordenar_listas(no_repetidos)
mayor_par = mayor_numero_par(no_repetidos)

print("\n FIN")
