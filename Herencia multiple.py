# Clase base 'A'
class A:
    def metodo_a(self):
        print("Método de A")

# Clase base 'B'
class B:
    def metodo_b(self):
        print("Método de B")

# Clase derivada 'C' que hereda de 'A' y 'B'
class C(A, B):
    def metodo_c(self):
        print("Método de C")

# Creación de objeto de tipo 'C'
objeto_c = C()

# Llamada a métodos de 'A', 'B' y 'C'
objeto_c.metodo_a()  # Método de A
objeto_c.metodo_b()  # Método de B
objeto_c.metodo_c()  # Método de C