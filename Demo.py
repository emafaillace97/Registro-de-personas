from Persona import Persona
from Registro import Registro


if __name__ == "__main__":
  reg = Registro()
  reg.agregar_persona(Persona("Ema","Faillace"))
  reg.mostrar_personas()
