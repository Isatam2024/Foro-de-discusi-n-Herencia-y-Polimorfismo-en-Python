# Clase base 'A'
class A:
    def metodo_a(self):
        print("Método de A")

# Clase derivada 'B' que hereda de 'A'
class B(A):
    def metodo_b(self):
        print("Método de B")

# Creación de objeto de tipo 'B'
objeto_b = B()

# Llamada a métodos de 'A' y 'B'
objeto_b.metodo_a()  # Método de A
objeto_b.metodo_b()  # Método de B