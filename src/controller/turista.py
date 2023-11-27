# Definición de la clase turista
class Turista():
  def __init__(self, persona, presupuesto, estadia) -> None:
    
    if (persona >= 1 and persona <= 2):
      self.persona = 'PER1'
    if (persona >= 3 and persona <= 4):
      self.persona = 'PER2'
    if (persona >= 5):
      self.persona = 'PER3'
    
    if (presupuesto >= 10000 and presupuesto <= 25000):
      self.presupuesto = 'PRB'
    if (presupuesto >= 25001 and presupuesto <= 60000):
      self.presupuesto = 'PRM'
    if (presupuesto >= 60001 and presupuesto <= 100000):
      self.presupuesto = 'PRA'

    if (estadia >= 1 and estadia <= 4):
      self.estadia = 'EST1'
    if (estadia >= 5 and estadia <= 12):
      self.estadia = 'EST2'
    if (estadia > 12):
      self.estadia = 'EST3'