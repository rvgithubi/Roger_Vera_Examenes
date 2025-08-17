from datetime import datetime

class Empleado:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = "peruana"
        self._contador=0

    def solicitar_nombre(self):
        return self.nombre

    def solicitar_edad(self):
        return self.edad

    def cumpleaños(self):
        self.edad = self.edad + 1
        return self.edad

    def incrementa(self):
        self._contador = self._contador + 1

    def aumentoSueldo(self):
        self._contador = self._contador + 1
        if self._contador == 2:
            self.sueldo = self.sueldo*0.3
            self.sueldo = self.sueldo + self.sueldo
        return self.sueldo

    def prediccion(self, año_futuro, edad_futura):
        if edad_futura < self.edad:
            return "Error: La edad ingresada es menor a la actual"
        año_actual = datetime.now().year
        años_restantes = edad_futura - self.edad
        año_resultado = año_actual + años_restantes
        return año_resultado,edad_futura


class Persona(Empleado):
    def __init__(self, nombre, edad, sueldo):
        self.saldo = sueldo

    def mostrar_saldo(self):
        return self.saldo

    def transferencia(self, monto, otro_empleado):
        if self.saldo < monto:
            return "Saldo insuficiente"
        self.saldo -= monto
        otro_empleado.saldo += monto
        return f"Transferencia exitosa. {self.mostrar_saldo()}"



empleado1 = Empleado("Juan", 25, 3000)


print("Nombre de Empleado :",empleado1.nombre)

print("\nAumentos de sueldo:")
print("Primer llamado:", empleado1.aumentoSueldo())  # No aplica aumento todavía
print("Segundo llamado:", empleado1.aumentoSueldo())  # Aplica el aumento del 30%
print("Tercer llamado:", empleado1.aumentoSueldo())   # Aplica otro aumento del 30%


print("La prediccion de los Años: ",empleado1.prediccion(2030,50))

persona1 = Persona("Carlos", 35, 5000)
persona2 = Persona("Luisa", 40, 6000)

print("Mostrando nuevo saldo :",persona1.mostrar_saldo())
