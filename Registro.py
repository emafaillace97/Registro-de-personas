class Registro:
    
    def __init__(self):
        self.__personas = []
    
    def agregar_persona(self, persona):
        self.__personas.append(persona)
    
    def eliminar_persona(self, persona):
        self.__personas.remove(persona)

if __name__ == "__main__": pass