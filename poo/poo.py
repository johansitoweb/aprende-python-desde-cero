# la poo es su siglas es prograacion orientada a objetos este es un tipo de paradigma
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

persona1 = Persona("Carlos", 30)
print(persona1.presentarse())

#La POO permite organizar el código en clases y objetos.