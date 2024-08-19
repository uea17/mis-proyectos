from abc import ABC, abstractmethod


# Abstracción
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


# Encapsulación y Herencia
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto

    def area(self):
        return self.__ancho * self.__alto

    def perimetro(self):
        return 2 * (self.__ancho + self.__alto)

    # Encapsulación: Métodos para modificar y acceder a los atributos privados
    def set_ancho(self, ancho):
        if ancho > 0:
            self.__ancho = ancho

    def get_ancho(self):
        return self.__ancho

    def set_alto(self, alto):
        if alto > 0:
            self.__alto = alto

    def get_alto(self):
        return self.__alto


# Herencia y Polimorfismo
class Circulo(Figura):
    def __init__(self, radio):
        self.__radio = radio

    def area(self):
        from math import pi
        return pi * (self.__radio ** 2)

    def perimetro(self):
        from math import pi
        return 2 * pi * self.__radio

    def set_radio(self, radio):
        if radio > 0:
            self.__radio = radio

    def get_radio(self):
        return self.__radio


def main():
    # Creación de objetos de diferentes clases
    figuras = [
        Rectangulo(4, 5),
        Circulo(3)
    ]

    # Polimorfismo: llamamos a métodos comunes a través de la referencia de la clase base
    for figura in figuras:
        print(f"{figura.__class__.__name__} - Área: {figura.area()}, Perímetro: {figura.perimetro()}")


if __name__ == "__main__":
    main()
