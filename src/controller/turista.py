# Definición de la clase turista
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