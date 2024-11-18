class Persona:

    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def get_nombre(self):
        return self.__nombre
    
    def __str__(self):
        return f"Nombre: {self.__nombre} - Apellido: {self.___apellido}"

if __name__ == "__main__": pass
