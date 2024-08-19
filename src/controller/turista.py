# Definición de la clase turista
from dataclasses import dataclass

@dataclass
class Turista:
  persona: str
  presupuesto: str
  estadia: str

  @classmethod
  def from_selections(cls, persona: int, presupuesto: int, estadia: int):
    persona_map = {
      0: 'PER1',
      1: 'PER2',
      2: 'PER3'
    }
    presupuesto_map = {
      0: 'PRB',
      1: 'PRM',
      2: 'PRA'
    }
    estadia_map = {
      0: 'EST1',
      1: 'EST2',
      2: 'EST3'
    }

    return cls (
      persona = persona_map.get(persona, 'PER3'),
      presupuesto = presupuesto_map.get(presupuesto, 'PRA'),
      estadia = estadia_map.get(estadia, 'EST3')
    )

"""
class Turista():
  def __init__(self, persona, presupuesto, estadia) -> None:
    
    if (persona == 0):
      self.persona = 'PER1'
    elif (persona == 1):
      self.persona = 'PER2'
    else:
      self.persona = 'PER3'
    
    if (presupuesto == 0):
      self.presupuesto = 'PRB'
    elif (presupuesto == 1):
      self.presupuesto = 'PRM'
    else:
      self.presupuesto = 'PRA'

    if (estadia == 0):
      self.estadia = 'EST1'
    elif (estadia == 1):
      self.estadia = 'EST2'
    else:
      self.estadia = 'EST3'
"""