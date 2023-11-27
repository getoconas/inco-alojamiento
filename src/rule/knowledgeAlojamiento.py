from experta import *

class turistas(Fact):
  pass

class servicios(Fact):
  pass

# Base de Conocimiento Alojamiento
class alojamiento_select(KnowledgeEngine):
  @DefFacts()
  def set_turista(self, _per, _pre, _esa):
    yield turistas(persona = _per, presupuesto = _pre, estadia = _esa)
    self.t_type = None

  @DefFacts()
  def set_servicio(self, _bpw, _est, _mas, _erl, _ing, _pis, _tar, _dis, _mat, _ser):
    yield servicios(bpwRule = _bpw, estRule = _est, masRule = _mas, erlRule = _erl, ingRule = _ing, pisRule = _pis, tarRule = _tar, disRule = _dis, matRule = _mat, serRule = _ser)
    self.s_type = None

  @DefFacts()
  def init_sequence(self):
    yield Fact(alojamiento = 'TA01')
    yield Fact(alojamiento = 'TA02')
    yield Fact(alojamiento = 'TA03')
    yield Fact(alojamiento = 'TA04')
    yield Fact(alojamiento = 'TA05')
    yield Fact(alojamiento = 'TA06')
    yield Fact(alojamiento = 'TA07')
    yield Fact(alojamiento = 'TA08')
    yield Fact(alojamiento = 'TA09')
    yield Fact(alojamiento = 'TA10')
    yield Fact(alojamiento = 'TA11')
    yield Fact(alojamiento = 'TA12')
    yield Fact(alojamiento = 'TA13')
    yield Fact(alojamiento = 'TA14')
    yield Fact(alojamiento = 'TA15')
    yield Fact(alojamiento = 'TA16')
    yield Fact(alojamiento = 'TA17')
    yield Fact(alojamiento = 'TA18')
    yield Fact(alojamiento = 'TA19')
    self.a_type = None
    
  # Definición de reglas  
  # Turistas
  @Rule (turistas(persona = 'PER2', presupuesto = 'PRB', estadia = 'EST1'))
  def turist1(self):
    self.declare(Fact(turist = 'TUR1'))
  
  @Rule (turistas(persona = 'PER1', presupuesto = 'PRB', estadia = 'EST2'))
  def turist2(self):
    self.declare(Fact(turist = 'TUR2'))

  @Rule (turistas(persona = 'PER2', presupuesto = 'PRM', estadia = 'EST1'))
  def turist3(self):
    self.declare(Fact(turist = 'TUR3'))

  @Rule (turistas(persona = 'PER2', presupuesto = 'PRM', estadia = 'EST2'))
  def turist4(self):
    self.declare(Fact(turist = 'TUR4'))

  @Rule (turistas(persona = 'PER1', presupuesto = 'PRM', estadia = 'EST3'))
  def turist5(self):
    self.declare(Fact(turist = 'TUR5'))
  
  @Rule (turistas(persona = 'PER1', presupuesto = 'PRA', estadia = 'EST1'))
  def turist6(self):
    self.declare(Fact(turist = 'TUR6'))

  @Rule (turistas(persona = 'PER3', presupuesto = 'PRA', estadia = 'EST2'))
  def turist7(self):
    self.declare(Fact(turist = 'TUR7'))

  @Rule (turistas(persona = 'PER3', presupuesto = 'PRA', estadia = 'EST3'))
  def turist8(self):
    self.declare(Fact(turist = 'TUR8'))

  # Servicios
  @Rule (servicios(bpwRule = 'BPW', estRule = 'EST', masRule = 'MAS', erlRule = None, ingRule = None, pisRule = None, tarRule = None, disRule = None, matRule = None, serRule = None))
  def service1(self):
    self.declare(Fact(service = 'SER1'))
  
  @Rule (servicios(bpwRule = None, estRule = None, masRule = 'MAS', erlRule = None, ingRule = None, pisRule = None, tarRule = None, disRule = 'DIS', matRule = None, serRule = 'SER'))
  def service2(self):
    self.declare(Fact(service = 'SER2'))
  
  @Rule (servicios(bpwRule = 'BPW', estRule = None, masRule = None, erlRule = None, ingRule = None, pisRule = 'PIS', tarRule = None, disRule = None, matRule = None, serRule = None))
  def service3(self):
    self.declare(Fact(service = 'SER3'))

  @Rule (servicios(bpwRule = None, estRule = None, masRule = None, erlRule = None, ingRule = None, pisRule = None, tarRule = None, disRule = None, matRule = 'MAT', serRule = 'SER'))
  def service4(self):
    self.declare(Fact(service = 'SER4'))

  @Rule (servicios(bpwRule = None, estRule = 'EST', masRule = None, erlRule = None, ingRule = None, pisRule = None, tarRule = 'TAR', disRule = None, matRule = None, serRule = None))
  def service5(self):
    self.declare(Fact(service = 'SER5'))

  @Rule (servicios(bpwRule = None, estRule = None, masRule = 'MAS', erlRule = None, ingRule = 'ING', pisRule = None, tarRule = None, disRule = None, matRule = None, serRule = None))
  def service6(self):
    self.declare(Fact(service = 'SER6'))

  @Rule (servicios(bpwRule = None, estRule = 'EST', masRule = None, erlRule = 'ERL', ingRule = None, pisRule = None, tarRule = None, disRule = None, matRule = None, serRule = None))
  def service7(self):
    self.declare(Fact(service = 'SER7'))

  @Rule (servicios(bpwRule = None, estRule = None, masRule = None, erlRule = None, ingRule = None, pisRule = None, tarRule = 'TAR', disRule = None, matRule = None, serRule = 'SER'))
  def service8(self):
    self.declare(Fact(service = 'SER8'))

  @Rule (servicios(bpwRule = 'BPW', estRule = None, masRule = None, erlRule = None, ingRule = None, pisRule = None, tarRule = None, disRule = None, matRule = None, serRule = None))
  def service9(self):
    self.declare(Fact(service = 'SER9'))

  @Rule (servicios(bpwRule = None, estRule = 'EST', masRule = None, erlRule = None, ingRule = None, pisRule = None, tarRule = None, disRule = None, matRule = None, serRule = None))
  def service10(self):
    self.declare(Fact(service = 'SER10'))

  @Rule (servicios(bpwRule = None, estRule = None, masRule = 'MAS', erlRule = None, ingRule = None, pisRule = None, tarRule = None, disRule = None, matRule = None, serRule = None))
  def service11(self):
    self.declare(Fact(service = 'SER11'))

  @Rule (servicios(bpwRule = None, estRule = None, masRule = None, erlRule = 'ERL', ingRule = None, pisRule = None, tarRule = None, disRule = None, matRule = None, serRule = None))
  def service12(self):
    self.declare(Fact(service = 'SER12'))

  @Rule (servicios(bpwRule = None, estRule = None, masRule = None, erlRule = None, ingRule = 'ING', pisRule = None, tarRule = None, disRule = None, matRule = None, serRule = None))
  def service13(self):
    self.declare(Fact(service = 'SER13'))
    
  @Rule (servicios(bpwRule = None, estRule = None, masRule = None, erlRule = None, ingRule = None, pisRule = None, tarRule = None, disRule = 'DIS', matRule = None, serRule = None))
  def service14(self):
    self.declare(Fact(service = 'SER14'))

  @Rule (servicios(bpwRule = None, estRule = None, masRule = None, erlRule = None, ingRule = None, pisRule = None, tarRule = None, disRule = None, matRule = None, serRule = 'SER'))
  def service15(self):
    self.declare(Fact(service = 'SER15'))

  # Alojamientos
  @Rule (AND(Fact(turist = 'TUR1'), Fact(service = 'SER1'), Fact(alojamiento = 'TA01')))
  def print_alojamiento1(self):
    self.a_type = 'TA01'
  
  @Rule (AND(Fact(turist = 'TUR1'), Fact(service = 'SER15'), Fact(alojamiento = 'TA02')))
  def print_alojamiento2(self):
    self.a_type = 'TA02'

  @Rule (AND(Fact(turist = 'TUR3'), Fact(service = 'SER14'), Fact(alojamiento = 'TA03')))
  def print_alojamiento3(self):
    self.a_type = 'TA03'

  @Rule (AND(Fact(turist = 'TUR2'), Fact(service = 'SER9'), Fact(alojamiento = 'TA04')))
  def print_alojamiento4(self):
    self.a_type = 'TA04'

  @Rule (AND(Fact(turist = 'TUR2'), Fact(service = 'SER11'), Fact(alojamiento = 'TA05')))
  def print_alojamiento5(self):
    self.a_type = 'TA05'

  @Rule (AND(Fact(turist = 'TUR3'), Fact(service = 'SER10'), Fact(alojamiento = 'TA06')))
  def print_alojamiento6(self):
    self.a_type = 'TA06'
  
  @Rule (AND(Fact(turist = 'TUR3'), Fact(service = 'SER15'), Fact(alojamiento = 'TA07')))
  def print_alojamiento7(self):
    self.a_type = 'TA07'

  @Rule (AND(Fact(turist = 'TUR3'), Fact(service = 'SER3'), Fact(alojamiento = 'TA08')))
  def print_alojamiento8(self):
    self.a_type = 'TA08'

  @Rule (AND(Fact(turist = 'TUR4'), Fact(service = 'SER15'), Fact(alojamiento = 'TA09')))
  def print_alojamiento9(self):
    self.a_type = 'TA09'

  @Rule (AND(Fact(turist = 'TUR4'), Fact(service = 'SER2'), Fact(alojamiento = 'TA10')))
  def print_alojamiento10(self):
    self.a_type = 'TA10'

  @Rule (AND(Fact(turist = 'TUR5'), Fact(service = 'SER15'), Fact(alojamiento = 'TA11')))
  def print_alojamiento11(self):
    self.a_type = 'TA11'
  
  @Rule (AND(Fact(turist = 'TUR5'), Fact(service = 'SER4'), Fact(alojamiento = 'TA12')))
  def print_alojamiento12(self):
    self.a_type = 'TA12'
  
  @Rule (AND(Fact(turist = 'TUR6'), Fact(service = 'SER5'), Fact(alojamiento = 'TA13')))
  def print_alojamiento13(self):
    self.a_type = 'TA13'

  @Rule (AND(Fact(turist = 'TUR7'), Fact(service = 'SER6'),Fact(alojamiento = 'TA14')))
  def print_alojamiento14(self):
    self.a_type = 'TA14'

  @Rule (AND(Fact(turist = 'TUR7'), Fact(service = 'SER7'), Fact(alojamiento = 'TA15')))
  def print_alojamiento15(self):
    self.a_type = 'TA15'

  @Rule (AND(Fact(turist = 'TUR8'), Fact(service = 'SER8'), Fact(alojamiento = 'TA16')))
  def print_alojamiento16(self):
    self.a_type = 'TA16'
  
  @Rule (AND(Fact(turist = 'TUR8'), Fact(service = 'SER13'), Fact(alojamiento = 'TA17')))
  def print_alojamiento17(self):
    self.a_type = 'TA17'

  @Rule (AND(Fact(turist = 'TUR8'), Fact(service = 'SER11'), Fact(alojamiento = 'TA18')))
  def print_alojamiento18(self):
    self.a_type = 'TA18'

  @Rule (AND(Fact(turist = 'TUR8'), Fact(service = 'SER12'), Fact(alojamiento = 'TA19')))
  def print_alojamiento19(self):
    self.a_type = 'TA19'