import wx
from experta import *

import src.controller.turista as turista
import src.controller.servicio as servicio
from src.data.alojamiento import listadoAlojamiento
import src.rule.knowledgeAlojamiento as conocimiento
    
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
    layout_child7 = wx.BoxSizer(wx.VERTICAL)
    layout_child8 = wx.BoxSizer(wx.HORIZONTAL)

    layout_child9 = wx.BoxSizer(wx.VERTICAL)
    layout_child10 = wx.BoxSizer(wx.HORIZONTAL)

    layout_child11 = wx.BoxSizer(wx.VERTICAL)

    self.listadoRecomendacion = []

    self.cbx_listado = wx.ComboBox(self, value = 'Alojamiento1')
    self.cbx_listado.SetEditable(False)
    self.cbx_listado.Bind(wx.EVT_TEXT, self.OnSelect)

    layout_child1.Add(self.cbx_listado, 0, wx.CENTER, 5)
    layout_main.Add(layout_child1, 0, wx.ALL | wx.EXPAND, 5)

    self.txt_result = wx.StaticText(self, label = 'Los alojamientos recomendados para usted son')

    layout_child2.Add(self.txt_result, 0, wx.ALL | wx.CENTER, 5)
    layout_main.Add(layout_child2, 0, wx.ALL | wx.EXPAND, 5)
    
    self.st_nombreAlojamiento = wx.StaticText(self, label = 'Nombre: ')
    layout_child3.Add(self.st_nombreAlojamiento, 0, wx.LEFT, 5)
    self.st_categoriaAlojamiento = wx.StaticText(self, label = 'Categoría: ')
    layout_child4.Add(self.st_categoriaAlojamiento, 0, wx.LEFT, 5)

    layout_child5.Add(layout_child3, 1, wx.ALL | wx.EXPAND, 5)
    layout_child5.Add(layout_child4, 1, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child5, 0, wx.ALL | wx.EXPAND, 5)

    self.st_precioAlojamiento = wx.StaticText(self, label = 'Precio: ')
    layout_child6.Add(self.st_precioAlojamiento, 0, wx.LEFT, 5)
    self.st_direccionAlojamiento = wx.StaticText(self, label = 'Direccion ')
    layout_child7.Add(self.st_direccionAlojamiento, 0, wx.LEFT, 5)

    layout_child8.Add(layout_child6, 1, wx.ALL | wx.EXPAND, 5)
    layout_child8.Add(layout_child7, 1, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child8, 0, wx.ALL | wx.EXPAND, 5)

    self.st_telefonoAlojamiento = wx.StaticText(self, label = 'Telefono ')
    layout_child9.Add(self.st_telefonoAlojamiento, 0, wx.LEFT, 5)
    layout_child10.Add(layout_child9, 1, wx.ALL | wx.EXPAND, 5)
    layout_main.Add(layout_child10, 0, wx.ALL | wx.EXPAND, 5)

    self.imageBitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(wx.Image('img/Cabana/Azul_Andino.png', wx.BITMAP_TYPE_ANY)))
    layout_child11.Add(self.imageBitmap, 0, wx.CENTER, 5)
    layout_main.Add(layout_child11, 0, wx.ALL | wx.EXPAND, 5)

    self.SetSizer(layout_main)

  # De acuerdo a la selccion del combobox se setean los valores de los campos que aparecen en el panel resultado
  def OnSelect(self, event):
    selected = self.cbx_listado.GetCurrentSelection()
    self.st_nombreAlojamiento.SetLabel('Nombre: ' + self.listadoRecomendacion[selected].nombre)
    self.st_categoriaAlojamiento.SetLabel('Categoria: ' + self.listadoRecomendacion[selected].categoria)
    self.st_precioAlojamiento.SetLabel('Precio: ' + self.listadoRecomendacion[selected].precio)
    self.st_direccionAlojamiento.SetLabel('Dirección: ' + self.listadoRecomendacion[selected].direccion)
    self.st_telefonoAlojamiento.SetLabel('Telefono: ' + str(self.listadoRecomendacion[selected].telefono))
    self.imageBitmap.SetBitmap(wx.BitmapFromImage(self.listadoRecomendacion[selected].imagen))

# Principal
class MainWindow(wx.Frame):
  def __init__(self):
    super().__init__(parent = None, size = (500, 450), title = 'Inicio')
    # Obtengo el listado de alojamientos
    self.listadoAlojamiento = listadoAlojamiento
    # Instancio la base de conocimiento
    self.alojamiento_recomendado = conocimiento.alojamiento_select()

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
        self.DeterminarListaAlojamiento(self.alojamiento_recomendado.a_type)
        if (len(self.pnl_resultado.listadoRecomendacion) == 0):
          wx.MessageBox('No hay ningún alojamiento disponible')
          return
        self.CargarRecomendacion()
        self.SetTitle('Resultado')
        self.pnl_inicio.Hide()
        self.pnl_resultado.Show()
        self.btn_main.SetLabel('Volver')
        self.SetSize(wx.Size(580, 550))
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

  # Se obtienen las recomendaciones ajustadas a los datos ingresados
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

    tur = turista.Turista(per_pnl, pre_pnl, est_pnl)
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

    ser = servicio.Servicio(bpw_cbx, est_cbx, mas_cbx, erl_cbx, ing_cbx, pis_cbx, tar_cbx, dis_cbx, mat_cbx, ser_cbx)
    return ser
    
# Definición principal de la aplicación
if __name__ == '__main__':
  app = wx.App()
  app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
  frame = MainWindow()
  frame.Show()
  app.MainLoop()

# TOCONAS, GASTON ENZO - GRUPO 10 - INCO
