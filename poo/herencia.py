# La herencia permite que una clase (llamada clase hija o subclase) herede atributos y métodos de otra clase (llamada clase padre o superclase). Esto ayuda a reutilizar el código y a crear una jerarquía de clases.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito en la subclase")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

mi_perro = Perro("Rex")
mi_gato = Gato("Miau")

print(f"{mi_perro.nombre} dice: {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} dice: {mi_gato.hacer_sonido()}")

#Explicación:

# La clase Animal es la clase padre.
# Las clases Perro y Gato heredan de Animal.
# Cada subclase implementa su propia versión del método hacer_sonido().