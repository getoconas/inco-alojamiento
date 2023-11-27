import wx
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

# Definción de la clase alojamiento
class Alojamiento():
  def __init__(self, nombre, categoria, precio, direccion, telefono, imagen, tipo) -> None:
    self.nombre = nombre
    self.categoria = categoria
    self.precio = precio
    self.direccion = direccion
    self.telefono = telefono
    self.imagen = imagen
    self.tipo = tipo

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
    self.spn_pre.SetRange(5000, 150000)

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

    layout_main = wx.BoxSizer(wx.VERTICAL)
    layout_child1 = wx.BoxSizer(wx.HORIZONTAL)
    layout_child2 = wx.BoxSizer(wx.HORIZONTAL)

    layout_child3 = wx.BoxSizer(wx.VERTICAL)
    layout_child4 = wx.BoxSizer(wx.VERTICAL)
    layout_child5 = wx.BoxSizer(wx.HORIZONTAL)

    layout_child6 = wx.BoxSizer(wx.VERTICAL)

    self.listadoRecomendacion = []

    self.cbx_listado = wx.ComboBox(self, value = 'Alojamiento1')
    self.cbx_listado.SetEditable(False)
    self.cbx_listado.Bind(wx.EVT_TEXT, self.OnSelect)

    layout_child1.Add(self.cbx_listado, 0, wx.ALL | wx.CENTER, 5)
    layout_main.Add(layout_child1, 0, wx.ALL | wx.EXPAND, 5)

    self.txt_result = wx.StaticText(self, label = 'Los alojamientos recomendados para usted son')

    layout_child2.Add(self.txt_result, 0, wx.ALL | wx.CENTER, 5)
    layout_main.Add(layout_child2, 0, wx.ALL | wx.EXPAND, 5)
    
    self.st_nombreAlojamiento = wx.StaticText(self, label = 'Nombre: ')
    layout_child3.Add(self.st_nombreAlojamiento, 0, wx.LEFT, 5)
    self.st_precioAlojamieno = wx.StaticText(self, label = 'Precio: ')
    layout_child4.Add(self.st_precioAlojamieno, 0, wx.LEFT, 5)

    layout_child5.Add(layout_child3, 1, wx.ALL | wx.EXPAND, 5)
    layout_child5.Add(layout_child4, 1, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child5, 0, wx.ALL | wx.EXPAND, 5)

    #self.st_direccionAlojamiento = wx.StaticText(self, label = 'Direccion ')
    #self.st_telefonoAlojamiento = wx.StaticText(self, label = 'Telefono ')

    self.imageBitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(wx.Image('img/Cabana/Azul_Andino.png', wx.BITMAP_TYPE_ANY)))

    layout_child6.Add(self.imageBitmap, 0, wx.CENTER, 5)
    layout_main.Add(layout_child6, 0, wx.ALL | wx.EXPAND, 5)

    self.SetSizer(layout_main)

  def OnSelect(self, event):
    selected = self.cbx_listado.GetCurrentSelection()

    self.imageBitmap.SetBitmap(wx.BitmapFromImage(self.listadoRecomendacion[selected].imagen))
    self.st_nombreAlojamiento.SetLabel('Nombre: ' + self.listadoRecomendacion[selected].nombre)

# Principal
class MainWindow(wx.Frame):
  def __init__(self):
    super().__init__(parent = None, size = (500, 450), title = 'Inicio')
    self.listadoAlojamiento = []
    self.GenerarAlojamiento()
    # Instancio la base de conocimiento
    self.alojamiento_recomendado = alojamiento_select()

    self.pnl_inicio = InputPanel(self)
    self.pnl_resultado = ResultPanel(self)
    
    self.btn_panel = wx.Panel(self)
    self.pnl_resultado.Hide()
    self.btn_main = wx.Button(self.btn_panel, label = 'Buscar')
    self.btn_main.Bind(wx.EVT_BUTTON, self.onSwitchPanels)

    self.sizer = wx.BoxSizer(wx.VERTICAL)
    self.btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

    self.btn_sizer.AddStretchSpacer(prop = 1)
    self.btn_sizer.Add(self.btn_main, 0, wx.ALIGN_CENTER, 5)
    self.btn_sizer.AddStretchSpacer(prop = 1)
    self.btn_panel.SetSizer(self.btn_sizer)

    self.sizer.Add(self.pnl_inicio, 1, wx.EXPAND)
    self.sizer.Add(self.pnl_resultado, 1, wx.EXPAND)
    self.sizer.Add(self.btn_panel, 1, wx.EXPAND)
    self.SetSizer(self.sizer)

  # Metodo para cambiar de ventana
  def onSwitchPanels(self, event):
    if self.pnl_inicio.IsShown():
      self.miTurista = self.ObtenerTurista() # Obtener Turista
      self.miServicio = self.ObtenerServico() # Obtener Servicio
      # Obtener Alojamiento
      self.alojamiento_recomendado.a_type = None
      self.alojamiento_recomendado.reset(
        _per = self.miTurista.persona,
        _pre = self.miTurista.presupuesto,
        _esa = self.miTurista.estadia,
        _bpw = self.miServicio.bpw,
        _est = self.miServicio.est,
        _mas = self.miServicio.mas,
        _erl = self.miServicio.erl,
        _ing = self.miServicio.ing,
        _pis = self.miServicio.pis,
        _tar = self.miServicio.tar,
        _dis = self.miServicio.dis,
        _mat = self.miServicio.mat,
        _ser = self.miServicio.ser
      )
      self.alojamiento_recomendado.run()
      if (self.alojamiento_recomendado.a_type != None):
        #wx.MessageBox('Datos OK', self.alojamiento_recomendado.a_type)
        self.DeterminarListaAlojamiento(self.alojamiento_recomendado.a_type)
        if (len(self.pnl_resultado.listadoRecomendacion) == 0):
          wx.MessageBox('No hay ningún alojamiento disponible')
          return
        self.CargarRecomendacion()
        self.SetTitle('Resultado')
        self.pnl_inicio.Hide()
        self.pnl_resultado.Show()
        self.btn_main.SetLabel('Volver')
        self.SetSize(wx.Size(700, 500))
      else:
        wx.MessageBox('Los datos ingresados no coinciden con ningún tipo de alojamiento')
    else:
      self.SetTitle('Inicio')
      self.pnl_resultado.Hide()
      self.pnl_inicio.Show()
      self.btn_main.SetLabel('Buscar')
      self.SetSize(wx.Size(500, 450))
    
    self.Layout()

  # Filtra el alojamiento de acuerdo al tipo de las reglas definidas
  def DeterminarListaAlojamiento(self, a_type):
    self.pnl_resultado.listadoRecomendacion = []
    for alo in self.listadoAlojamiento:
      if (alo.tipo == a_type):
        self.pnl_resultado.listadoRecomendacion.append(alo)

  # 
  def CargarRecomendacion(self):
    self.pnl_resultado.cbx_listado.Clear()
    
    for alo in self.pnl_resultado.listadoRecomendacion:
      self.pnl_resultado.cbx_listado.Append(alo.nombre)
    self.pnl_resultado.cbx_listado.SetSelection(0)
    self.pnl_resultado.OnSelect(event = wx.EVT_TEXT)
    self.pnl_resultado.imageBitmap.SetBitmap(wx.BitmapFromImage(self.pnl_resultado.listadoRecomendacion[0].imagen))


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
  def GenerarAlojamiento(self):
    # TA01
    self.listadoAlojamiento.append(Alojamiento('Eco Cabaña', 'Cabaña', '10000 a 25000', 'Av. San Martín S/N', 3885108936, wx.Image('img/Cabana/Eco_Cabaña.png'), 'TA01'))
    self.listadoAlojamiento.append(Alojamiento('Mirador del Virrey', 'Cabaña', '10000 a 25000', 'Ex Ruta 52 - KM 4,4 - Chalala', 3885904057, wx.Image('img/Cabana/Mirador_del_Virrey_Cabaña_Boutique.png'), 'TA01'))
    # TA02
    self.listadoAlojamiento.append(Alojamiento('Camping Coquena', 'Camping/Cabaña', '10000 a 25000', 'Av. San Martín S/N', 3885108936, wx.Image('img/Cabana/Camping_Coquena.png'), 'TA02'))
    self.listadoAlojamiento.append(Alojamiento('Cabañas y Camping Familiar Rodolfo', 'Camping/Cabaña', '10000 a 25000', 'Ruta 52 S/N', 3884349307, wx.Image('img/Cabana/Mirador_del_Virrey_Cabaña_Boutique.png'), 'TA02'))
    self.listadoAlojamiento.append(Alojamiento('La Posada de Candelaria', 'Hostal', '16000', 'Libertad S/N', 3885879786, wx.Image('img/Hostel/La_Posada_de_la_Candelaria.png'), 'TA02'))
    self.listadoAlojamiento.append(Alojamiento('Pumac', 'Hostal', '20500', 'Pantaleón Cruz S/N', 3885089048, wx.Image('img/Hostel/Pumac.png'), 'TA02'))
    # TA03
    self.listadoAlojamiento.append(Alojamiento('Posada El Molle', 'Hostal', '27000', 'Florida 203', 3885043867, wx.Image('img/Hostel/Posada_el_Molle.png'), 'TA03'))
    # TA04
    self.listadoAlojamiento.append(Alojamiento('Mama Coca', 'Hostal', '10000 a 25000', 'Libertad S/N', 3884908434, wx.Image('img/Hostel/MamaCoca.png'), 'TA04'))
    self.listadoAlojamiento.append(Alojamiento('El Rincón del Oso', 'Hostal', '10000 a 25000', 'Florida 209', 3886049255, wx.Image('img/Hostel/El_Rincon_del_Oso.png'), 'TA04'))
    self.listadoAlojamiento.append(Alojamiento('Pumac', 'Hostal', '20500', 'Pantaleón Cruz S/N', 3885089048, wx.Image('img/Hostel/Pumac.png'), 'TA04'))
    self.listadoAlojamiento.append(Alojamiento('INTI KAY', 'Hostal', '10000 a 25000', 'Florida esq. Belgrano', 3884076204, wx.Image('img/Hostel/INTI_KAY.png'), 'TA04'))
    # TA05
    self.listadoAlojamiento.append(Alojamiento('Mama Coca', 'Hostal', '10000 a 25000', 'Libertad S/N', 3884908434, wx.Image('img/Hostel/MamaCoca.png'), 'TA05'))
    self.listadoAlojamiento.append(Alojamiento('Doña Velia', 'Hostal', '10000 a 25000', 'Florida S/N', 3884967488, wx.Image('img/Hostel/Doña_Velia.png'), 'TA05'))
    self.listadoAlojamiento.append(Alojamiento('El Refugio de Noe', 'Hostal', '10000', 'Salta esq Gorriti', 3884803503, wx.Image('img/Hostel/El_Refugio_de_Noe.png'), 'TA05'))
    # TA06
    self.listadoAlojamiento.append(Alojamiento('Aguas Coloradas', 'Hostería', '26000 a 60000', 'Av. San Martín S/N', 3884975583, wx.Image('img/Hosteria/Aguas_Coloradas.png'), 'TA06'))
    # TA07
    self.listadoAlojamiento.append(Alojamiento('Nido de Cóndores', 'Hotel', '26000 a 60000', 'San Ramón Ote 1265', 569822092395, wx.Image('img/Hotel/Nido_de_Condores.png'), 'TA07'))
    self.listadoAlojamiento.append(Alojamiento('La Pushka', 'Hostería', '26000 a 60000', 'Pasaje Santa Rosa S/N', 3885170350, wx.Image('img/Hosteria/La_Pushka.png'), 'TA07'))
    self.listadoAlojamiento.append(Alojamiento('Wara Wara', '26000 a 60000', 'Av. San Martín S/N', 3884780516, wx.Image('img/Hosteria/Wara_Wara.png'), 'TA07'))
    # TA08
    self.listadoAlojamiento.append(Alojamiento('Killari', wx.Image('img/Hotel/Hotel_Killari.png'), 'TA08'))
    # TA09
    self.listadoAlojamiento.append(Alojamiento('Hotel Cactus Cerros', wx.Image('img/Hotel/Hotel_Cactus_Cerro.png'), 'TA09'))
    self.listadoAlojamiento.append(Alojamiento('La Valentina', wx.Image('img/Hotel/La_Valentina.png'), 'TA09'))
    self.listadoAlojamiento.append(Alojamiento('Las Lavandas Purmamarca', wx.Image('img/Hotel/Las_Lavandas_Purmamarca.png'), 'TA09'))
    self.listadoAlojamiento.append(Alojamiento('MAI JAII', wx.Image('img/Hotel/MAI_JAII.png'), 'TA09'))
    self.listadoAlojamiento.append(Alojamiento('Tierra Virgen Apartaments', wx.Image('img/Hotel/Tierra_Virgen.png'), 'TA09'))
    self.listadoAlojamiento.append(Alojamiento('Aguas Coloradas', wx.Image('img/Hosteria/Aguas_Coloradas.png'), 'TA09'))
    self.listadoAlojamiento.append(Alojamiento('La Casa Encantanda', wx.Image('img/Hosteria/La_Casa_Encantada.png'), 'TA09'))
    self.listadoAlojamiento.append(Alojamiento('La Pushka', wx.Image('img/Hosteria/La_Pushka.png'), 'TA09'))
    # TA10
    self.listadoAlojamiento.append(Alojamiento('Nido de Cóndores', wx.Image('img/Hotel/Nido_de_Condores.png'), 'TA10'))
    # TA11
    self.listadoAlojamiento.append(Alojamiento('Los Agustinos', wx.Image('img/Hotel/Los_Agustinos.png'), 'TA11'))
    self.listadoAlojamiento.append(Alojamiento('Tierra Virgen Apartaments', wx.Image('img/Hotel/Tierra_Virgen.png'), 'TA11'))
    self.listadoAlojamiento.append(Alojamiento('Las Vicuñas', wx.Image('img/Hotel/Las_Vicuñas.png'), 'TA11'))
    self.listadoAlojamiento.append(Alojamiento('El Viejo Algarrobo', wx.Image('img/Hosteria/El_Viejo_Algarrobo.png'), 'TA11'))
    self.listadoAlojamiento.append(Alojamiento('Del Amauta', wx.Image('img/Hosteria/Del_Amauta.png'), 'TA11'))
    # TA12
    self.listadoAlojamiento.append(Alojamiento('Terrazas de la Posta Purmamarca', wx.Image('img/Hosteria/Terraza_La_Posta.png'), 'TA11'))
    # TA13
    self.listadoAlojamiento.append(Alojamiento('Huara Huasi', wx.Image('img/Hosteria/Huara_Huasi.png'), 'TA13'))
    # TA14
    self.listadoAlojamiento.append(Alojamiento('Luna Jatun', wx.Image('img/Hotel/Luna_Jatun.png'), 'TA14'))
    self.listadoAlojamiento.append(Alojamiento('Aguas Coloradas', wx.Image('img/Hosteria/Aguas_Coloradas.png'), 'TA14'))
    # TA15
    self.listadoAlojamiento.append(Alojamiento('El Manatial del Silencio', wx.Image('img/Hotel/El_Manantial_del_Silencio.png'), 'TA15'))
    self.listadoAlojamiento.append(Alojamiento('La Comarca', wx.Image('img/Hotel/La_Comarca.png'), 'TA15'))
    self.listadoAlojamiento.append(Alojamiento('Marquez de Tojo', wx.Image('img/Hotel/Marquez_de_Tojo.png'), 'TA15'))
    self.listadoAlojamiento.append(Alojamiento('Colores de Purmamarca', wx.Image('img/Hotel/Colores_de_Purmamarca.png'), 'TA15'))
    self.listadoAlojamiento.append(Alojamiento('El Refugio de Coquena', wx.Image('img/Hotel/El_Refugio_de_Coquena.png'), 'TA15'))
    # TA16
    self.listadoAlojamiento.append(Alojamiento('Los Colorados Cabañas Botique', wx.Image('img/Cabana/Los_Colorados.png'), 'TA16'))
    self.listadoAlojamiento.append(Alojamiento('Azul Andino', wx.Image('img/Cabana/Azul_Andino.png'), 'TA16'))
    self.listadoAlojamiento.append(Alojamiento('La Reliquia', wx.Image('img/Hotel/La_Reliquia.png'), 'TA16'))
    # TA17
    self.listadoAlojamiento.append(Alojamiento('Luna Jatun', wx.Image('img/Hotel/Luna_Jatun.png'), 'TA17'))
    # TA18
    self.listadoAlojamiento.append(Alojamiento('Colores de Purmamarca', wx.Image('img/Hotel/Colores_de_Purmamarca.png'), 'TA18'))
    self.listadoAlojamiento.append(Alojamiento('El Cielo de Purmamarca', wx.Image('img/Hotel/El_Cielo_de_Purmamarca.png'), 'TA18'))
    self.listadoAlojamiento.append(Alojamiento('Luna Jatun', wx.Image('img/Hotel/Luna_Jatun.png'), 'TA18'))
    # TA19
    self.listadoAlojamiento.append(Alojamiento('La Comarca', wx.Image('img/Hotel/La_Comarca.png'), 'TA19'))
    self.listadoAlojamiento.append(Alojamiento('Luna Jatun', wx.Image('img/Hotel/Luna_Jatun.png'), 'TA19'))
    self.listadoAlojamiento.append(Alojamiento('Pumahuasi Hotel Boutique', wx.Image('img/Hotel/Pumahuasi_Hotel_Boutique.png'), 'TA19'))

# Definición principal de la aplicación
if __name__ == '__main__':
  app = wx.App()
  app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
  frame = MainWindow()
  frame.Show()
  app.MainLoop()

# TOCONAS, GASTON ENZO - GRUPO 10 - INCO
