# Definición de la clase alojamiento
from dataclasses import dataclass

@dataclass
class Alojamiento:
  nombre: str
  categoria: str
  precio: int
  direccion: str
  telefono: int
  imagen: str
  tipo: str
