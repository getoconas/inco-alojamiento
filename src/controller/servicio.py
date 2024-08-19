# Definición de la clase servicio
from dataclasses import dataclass

@dataclass
class Servicio:
  bpw: str = None
  est: str = None
  mas: str = None
  erl: str = None
  ing: str = None
  pis: str = None
  tar: str = None
  dis: str = None
  mat: str = None
  ser: str = None

  @classmethod
  def from_flags(cls, bpw=False, est=False, mas=False, erl=False, ing=False, pis=False, tar=False, dis=False, mat=False, ser=False):
    return cls(
      bpw='BPW' if bpw else None,
      est='EST' if est else None,
      mas='MAS' if mas else None,
      erl='ERL' if erl else None,
      ing='ING' if ing else None,
      pis='PIS' if pis else None,
      tar='TAR' if tar else None,
      dis='DIS' if dis else None,
      mat='MAT' if mat else None,
      ser='SER' if ser else None
    )
