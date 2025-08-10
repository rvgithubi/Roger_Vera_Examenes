"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
  usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
  conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
  tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
  tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
  salario, según corresponda.
"""

nombre = "Roger Vera"
salario = 1000
edad = "25"
compania = "IBM"
print("La variable nombre   tipo: ", type(nombre))
print("La variable salario  tipo: ", type(salario))
print("La variable edad     tipo: ", type(edad))
print("La variable compania tipo: ", type(compania))


if int(edad) > 30:
    print("\nUsted tiene un bono de 10% en el mes de diciembre")
    bono = (salario ** 2) + (salario*10)/100
else:
    print("\nUsted tiene un bono de 5% en el mes de diciembre")
    bono = salario ** 2 + (salario*5)/100


print("Su bono es de: ", bono)