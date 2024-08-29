from abc import ABC, abstractmethod
class Vehiculo(ABC):  #se crea la clase vehiculo
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"


# Clase concreta Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas

    def arrancar(self):
        print("El coche arranca")

    def frenar(self):
        print("El coche frena")

    def __str__(self):
        return super().__str__() + f" con {self.num_puertas} puertas"


# Clase concreta Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def arrancar(self):
        print("La moto arranca")

    def frenar(self):
        print("La moto frena")

    def __str__(self):
        return super().__str__() + f" con {self.cilindrada} cc"


# Crear instancias de Coche y Moto
coche = Coche("Toyota", "Corolla", 2015, 4)
moto = Moto("Honda", "CBR500R", 2020, 500)

print(coche)
coche.arrancar()
coche.frenar()

print(moto)
moto.arrancar()
moto.frenar()