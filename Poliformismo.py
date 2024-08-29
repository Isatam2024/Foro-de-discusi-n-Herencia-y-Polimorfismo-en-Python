#
class Empleado:
    def calcular_salario(self):
        pass

# Clase derivada 'Gerente'
class Gerente(Empleado):
    def calcular_salario(self):
        print("El gerente cobra un salario de $5000")

# Clase derivada 'Desarrollador'
class Desarrollador(Empleado):
    def calcular_salario(self):
        print("El desarrollador cobra un salario de $3000")

# Creación de objetos y llamada al método 'calcular_salario()'
for empleado in [Gerente(), Desarrollador()]:
    empleado.calcular_salario()