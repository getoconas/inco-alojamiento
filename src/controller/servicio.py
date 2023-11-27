# Definición de la clase servicio
class Servicio():
  def __init__(self, bpw, est, mas, erl, ing, pis, tar, dis, mat, ser) -> None:
    if (bpw):
      self.bpw = 'BPW'
    else:
      self.bpw = None
    if (est):
      self.est = 'EST'
    else:
      self.est = None
    if (mas):
      self.mas = 'MAS'
    else:
      self.mas = None
    if (erl):
      self.erl = 'ERL'
    else:
      self.erl = None
    if (ing):
      self.ing = 'ING'
    else:
      self.ing = None
    if (pis):
      self.pis = 'PIS'
    else:
      self.pis = None
    if (tar):
      self.tar = 'TAR'
    else:
      self.tar = None
    if (dis):
      self.dis = 'DIS'
    else:
      self.dis = None
    if (mat):
      self.mat = 'MAT'
    else:
      self.mat = None
    if (ser):
      self.ser = 'SER'
    else:
      self.ser = None