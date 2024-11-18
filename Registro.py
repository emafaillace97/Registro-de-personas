class Registro:
    
    def __init__(self):
        self.__personas = []
    
    def agregar_persona(self, persona):
        self.__personas.append(persona)
    
    def eliminar_persona(self, persona):
        self.__personas.remove(persona)
    
    def mostrar_personas(self):
        for persona in self.__personas:
            print(persona)

if __name__ == "__main__": pass