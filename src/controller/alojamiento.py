# Definción de la clase alojamiento
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

"""
class Alojamiento():
  def __init__(self, nombre, categoria, precio, direccion, telefono, imagen, tipo) -> None:
    self.nombre = nombre
    self.categoria = categoria
    self.precio = precio
    self.direccion = direccion
    self.telefono = telefono
    self.imagen = imagen
    self.tipo = tipo
"""