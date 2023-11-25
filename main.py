import wx
from experta import *

class turistas(Fact):
  pass

class servicios(Fact):
  pass

class Alojamiento(KnowledgeEngine):
  @DefFacts()
  def set_turista(self, _per, _pre, _est):
    yield turistas(persona = _per, presupuesto = _pre, estadia = _est)
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
  @Rule (turistas(persona = 'PER1', presupuesto = 'PRB', estadia = 'EST1'))
  def turist1(self):
    self.declare(Fact(turist = 'TUR1'))
  
  @Rule (turistas(persona = 'PER2', presupuesto = 'PRB', estadia = 'EST2'))
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
  @Rule (servicios(bpwRule = 'BPW', estRule = 'EST', masRule = 'MAS'))
  def service1(self):
    self.declare(Fact(service = 'SER1'))

  @Rule (servicios(masRule = 'MAS', disRule = 'DIS', serRule = 'SER'))
  def service2(self):
    self.declare(Fact(service = 'SER2'))
  
  @Rule (servicios(bpwRule = 'BPW', pisRule = 'PIS'))
  def service3(self):
    self.declare(Fact(service = 'SER3'))

  @Rule (servicios(matRule = 'MAT', serRule = 'SER'))
  def service4(self):
    self.declare(Fact(service = 'SER4'))

  @Rule (servicios(estRule = 'EST', tarRule = 'TAR'))
  def service5(self):
    self.declare(Fact(service = 'SER5'))

  @Rule (servicios(masRule = 'MAS', ingRule = 'ING'))
  def service6(self):
    self.declare(Fact(service = 'SER6'))

  @Rule (servicios(estRule = 'EST', erlRule = 'ERL'))
  def service7(self):
    self.declare(Fact(service = 'SER7'))

  @Rule (servicios(tarRule = 'TAR', serRule = 'SER'))
  def service8(self):
    self.declare(Fact(service = 'SER8'))

  @Rule (servicios(bpwRule = 'BPW'))
  def service9(self):
    self.declare(Fact(service = 'SER9'))

  @Rule (servicios(estRule = 'EST'))
  def service10(self):
    self.declare(Fact(service = 'SER10'))

  @Rule (servicios(masRule = 'MAS'))
  def service11(self):
    self.declare(Fact(service = 'SER11'))

  @Rule (servicios(erlRule = 'ERL'))
  def service12(self):
    self.declare(Fact(service = 'SER12'))

  @Rule (servicios(ingRule = 'ING'))
  def service13(self):
    self.declare(Fact(service = 'SER13'))

  @Rule (servicios(disRule = 'DIS'))
  def service14(self):
    self.declare(Fact(service = 'SER14'))

  @Rule (servicios(serRule = 'SER'))
  def service15(self):
    self.declare(Fact(service = 'SER15'))

  # Alojamientos
  @Rule (AND(Fact(turist = 'TUR1'), Fact(service = 'SER1'), Fact(alojamiento = 'TA01')))
  def print_alojamiento1(self):
    self.a_type = 'TA01'
  
  @Rule (AND(Fact(turist = 'TUR2'), Fact(service = 'SER15'), Fact(alojamiento = 'TA02')))
  def print_alojamiento2(self):
    self.a_type = 'TA02'

  @Rule (AND(Fact(turist = 'TUR1'), Fact(service = 'SER14'), Fact(alojamiento = 'TA03')))
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

  @Rule (AND(Fact(turist = 'TUR7'), Fact(service = 'SER6'), Fact(alojamiento = 'TA14')))
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

# Definición de la clase turista
class Turista():
  def __init__(self, persona, presupuesto, estadia) -> None:
    
    if (persona >= 1 and persona <= 2):
      self.persona = 'PER1'
    if (persona >= 3 and persona <= 4):
      self.persona = 'PER2'
    if (persona >= 5):
      self.persona = 'PER3'
    
    self.presupuesto = presupuesto

    self.estadia = estadia

# Definición de la clase servicio
class Servicio():
  def __init__(self, bpw, est, mas, erl, ing, pis, tar, dis, mat, ser) -> None:
    self.bpw = bpw
    self.est = est
    self.mas = mas
    self.erl = erl
    self.ing = ing
    self.pis = pis
    self.tar = tar
    self.dis = dis
    self.mat = mat
    self.ser = ser

# Definción de la clase alojamiento
class Alojamiento():
  def __init__(self, nombre, precio, tipo, imagen) -> None:
    self.nombre = nombre
    self.precio = precio
    self.tipo = tipo
    self.imagen = imagen

# Pantalla de Inicio - Ingreso de Datos
class InputPanel(wx.Panel):
  def __init__(self, parent):
    wx.Panel.__init__(self, parent = parent)

    layout_main = wx.BoxSizer(wx.VERTICAL) 

    layout_child1 = wx.BoxSizer(wx.VERTICAL)
    layout_child2 = wx.BoxSizer(wx.VERTICAL)
    layout_child3 = wx.BoxSizer(wx.VERTICAL)

    layout_child4 = wx.BoxSizer(wx.VERTICAL)
    layout_child5 = wx.BoxSizer(wx.VERTICAL)
    layout_child6 = wx.BoxSizer(wx.HORIZONTAL)

    layout_child7 = wx.BoxSizer(wx.VERTICAL)
    layout_child8 = wx.BoxSizer(wx.VERTICAL)
    layout_child9 = wx.BoxSizer(wx.HORIZONTAL)

    layout_child10 = wx.BoxSizer(wx.VERTICAL)
    layout_child11 = wx.BoxSizer(wx.VERTICAL)
    layout_child12 = wx.BoxSizer(wx.HORIZONTAL)

    layout_child13 = wx.BoxSizer(wx.VERTICAL)
    layout_child14 = wx.BoxSizer(wx.VERTICAL)
    layout_child15 = wx.BoxSizer(wx.HORIZONTAL)

    layout_child16 = wx.BoxSizer(wx.VERTICAL)
    layout_child17 = wx.BoxSizer(wx.VERTICAL)
    layout_child18 = wx.BoxSizer(wx.HORIZONTAL)

    # Cantidad de personas
    self.txt_per = wx.StaticText(self, label = 'Cantidad de personas', style = wx.ALIGN_LEFT)
    self.spn_per = wx.SpinCtrl(self, value = '1')

    layout_child1.Add(self.txt_per, 0, wx.LEFT, 5)
    layout_child1.Add(self.spn_per, 0, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child1, 0, wx.ALL | wx.EXPAND, 5)

    # Presupuesto
    self.txt_pre = wx.StaticText(self, label = 'Presupuesto', style = wx.ALIGN_LEFT)
    self.spn_pre = wx.SpinCtrl(self, value = '10000')

    layout_child2.Add(self.txt_pre, 0, wx.LEFT, 5)
    layout_child2.Add(self.spn_pre, 0, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child2, 0, wx.ALL | wx.EXPAND, 5)

    # Tiempo de estadía
    self.txt_est = wx.StaticText(self, label = 'Tiempo de Estadía', style = wx.ALIGN_LEFT)
    self.spn_est = wx.SpinCtrl(self, value = '1')

    layout_child3.Add(self.txt_est, 0, wx.LEFT, 5)
    layout_child3.Add(self.spn_est, 0, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child3, 0, wx.ALL | wx.EXPAND, 5)

    # Checkbox BPW - EST
    self.cbx_bpw = wx.CheckBox(self, label = "Baño Privado y WiFi")
    layout_child4.Add(self.cbx_bpw, 0, wx.LEFT, 5)

    self.cbx_est = wx.CheckBox(self, label = "Estacionamiento")
    layout_child5.Add(self.cbx_est, 0, wx.LEFT, 5)

    layout_child6.Add(layout_child4, 1, wx.ALL | wx.EXPAND, 5)
    layout_child6.Add(layout_child5, 1, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child6, 0, wx.ALL | wx.EXPAND, 5)

    # Checkbox MAS - ERL
    self.cbx_mas = wx.CheckBox(self, label = "Aceptan Mascotas")
    layout_child7.Add(self.cbx_mas, 0, wx.LEFT, 5)

    self.cbx_erl = wx.CheckBox(self, label = "Serv. de Entre., Restaurante y Limpieza")
    layout_child8.Add(self.cbx_erl, 0, wx.LEFT, 5)

    layout_child9.Add(layout_child7, 1, wx.ALL | wx.EXPAND, 5)
    layout_child9.Add(layout_child8, 1, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child9, 0, wx.ALL | wx.EXPAND, 5)

    # Checkbox ING - PIS
    self.cbx_ing = wx.CheckBox(self, label = "Asist. en Inglés")
    layout_child10.Add(self.cbx_ing, 0, wx.LEFT, 5)

    self.cbx_pis = wx.CheckBox(self, label = "Piscina")
    layout_child11.Add(self.cbx_pis, 0, wx.LEFT, 5)

    layout_child12.Add(layout_child10, 1, wx.ALL | wx.EXPAND, 5)
    layout_child12.Add(layout_child11, 1, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child12, 0, wx.ALL | wx.EXPAND, 5)

    # Checkbox TAR - DIS
    self.cbx_tar = wx.CheckBox(self, label = "Pago con Tarjeta")
    layout_child13.Add(self.cbx_tar, 0, wx.LEFT, 5)

    self.cbx_dis = wx.CheckBox(self, label = "Acc. para Personas Discapacitadas")
    layout_child14.Add(self.cbx_dis, 0, wx.LEFT, 5)

    layout_child15.Add(layout_child13, 1, wx.ALL | wx.EXPAND, 5)
    layout_child15.Add(layout_child14, 1, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child15, 0, wx.ALL | wx.EXPAND, 5)

    # Checkbox MAT - SER
    self.cbx_mat = wx.CheckBox(self, label = "Solo Matrimonio")
    layout_child16.Add(self.cbx_mat, 0, wx.LEFT, 5)

    self.cbx_ser = wx.CheckBox(self, label = "Otros Servicios")
    layout_child17.Add(self.cbx_ser, 0, wx.LEFT, 5)

    layout_child18.Add(layout_child16, 1, wx.ALL | wx.EXPAND, 5)
    layout_child18.Add(layout_child17, 1, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child18, 0, wx.ALL | wx.EXPAND, 5)
    
    self.SetSizer(layout_main)

# Panel Recomendación Alojamiento
class ResultPanel(wx.Panel):
  def __init__(self, parent):
    wx.Panel.__init__(self, parent = parent)


# Principal
class MainWindow(wx.Frame):
  def __init__(self):
    super().__init__(parent = None, size = (500, 450), title = 'Inicio')
    self.listadoAlojamiento = []

    self.pnl_inicio = InputPanel(self)
    #self.pnl_resultado = ResultPanel(self)

  # Metodo para cambiar de ventana
  def onSwitchPanels(self, event):
    if self.pnl_inicio.IsShown():
      # Determinar tipo de turista
      self.miTurista = self.ObtenerTurista()
      # Obtener servicios
      self.miServicio = self.ObtenerServico()


  # Metodo para obtener los datos del turista ingresado
  def ObtenerTurista(self):
    per_pnl = self.pnl_inicio.spn_per.GetValue()
    pre_pnl = self.pnl_inicio.spn_pre.GetValue()
    est_pnl = self.pnl_inicio.spn_est.GetValue()

    tur = Turista(per_pnl, pre_pnl, est_pnl)
    return tur
  
  # Metodo para obtener los servicios seleccionados
  def ObtenerServico(self):
    bpw_cbx = self.pnl_inicio.cbx_bpw.IsChecked()
    est_cbx = self.pnl_inicio.cbx_est.IsChecked()
    mas_cbx = self.pnl_inicio.cbx_mas.IsChecked()
    erl_cbx = self.pnl_inicio.cbx_erl.IsChecked()
    ing_cbx = self.pnl_inicio.cbx_ing.IsChecked()
    pis_cbx = self.pnl_inicio.cbx_pis.IsChecked()
    tar_cbx = self.pnl_inicio.cbx_tar.IsChecked()
    dis_cbx = self.pnl_inicio.cbx_dis.IsChecked()
    mat_cbx = self.pnl_inicio.cbx_mat.IsChecked()
    ser_cbx = self.pnl_inicio.cbx_ser.IsChecked()

    ser = Servicio(bpw_cbx, est_cbx, mas_cbx, erl_cbx, ing_cbx, pis_cbx, tar_cbx, dis_cbx, mat_cbx, ser_cbx)
    return ser

  # Metodo para generar y carga de alojamiento
  #def GenerarAlojamiento(self):
    

# Definición principal de la aplicación
if __name__ == '__main__':
  app = wx.App()
  app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
  frame = MainWindow()
  frame.Show()
  app.MainLoop()
