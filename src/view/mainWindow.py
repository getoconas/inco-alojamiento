import wx

import src.controller.turista as turista
import src.controller.servicio as servicio
from src.data.alojamiento import listadoAlojamiento
import src.rule.knowledgeAlojamiento as conocimiento
import src.view.panel.inputPanel as inputPanel
import src.view.panel.resultPanel as resultPanel
   
# Main Window
class MainWindow(wx.Frame):
  def __init__(self):
    super().__init__(parent = None, size = (500, 450), title = 'Inicio')
    # Obtengo el listado de alojamientos
    self.listadoAlojamiento = listadoAlojamiento
    # Instancio la base de conocimiento
    self.alojamiento_recomendado = conocimiento.alojamiento_select()

    self.pnl_inicio = inputPanel.InputPanel(self)
    self.pnl_resultado = resultPanel.ResultPanel(self)
    
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
    per_pnl = self.pnl_inicio.cbx_personas.GetSelection()
    pre_pnl = self.pnl_inicio.cbx_presupuesto.GetSelection()
    est_pnl = self.pnl_inicio.cbx_estadia.GetSelection()
    
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