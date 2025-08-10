"""
- Caso: Calculadora de propinas
Crea un programa que permita ingresar el total de una cuenta en un restaurante,
el porcentaje de propina que desea dejar el cliente y el número de personas que
dividirán la cuenta. El programa debe mostrar:
El monto total con propina.
El monto que debe pagar cada persona (con 2 decimales).
Un mensaje será personalizado, indicará si el monto individual supera los 100
soles, mostrando un mensaje de advertencia si es el caso.
Entrada esperada (por input):
Total de la cuenta: float
Porcentaje de propina: float
Número de personas: int
Salida ejemplo (output):
   Monto total con propina: S/. 230.00
   Cada persona debe pagar: S/. 115.00
   ¡Advertencia! El monto por persona supera los S/. 100

"""

total_cuenta = float(input("Total de la cuenta: S/. "))
porcentaje_propina = float(input("Porcentaje de propina (%): "))
num_personas = int(input("Número de personas: "))


propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + propina
monto_por_persona = total_con_propina / num_personas

# Resultados
print("Monto total con propina: S/. ", format(total_con_propina, '.2f'))
print("Cada persona debe pagar: S/. ", format(monto_por_persona, '.2f'))
print("------------------------------------")

if monto_por_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")
