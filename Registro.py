from Persona import Persona


class Registro:
    
    def __init__(self):
        self.__personas = []
    
    def agregar_persona(self, persona):
        if isinstance(persona, Persona):
            self.__personas.append(persona)
        else:
            raise TypeError("No es una instacia de tipo Persona")
        
    def eliminar_persona(self, persona):
        if isinstance(persona, Persona):
            self.__personas.remove(persona)
        raise TypeError("No es una instacia de tipo Persona")
    
    def mostrar_personas(self):
        for persona in self.__personas:
            print(persona)

if __name__ == "__main__": pass
