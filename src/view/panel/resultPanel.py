import wx

# Panel Recomendación de Alojamiento
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

    layout_child1.Add(self.cbx_listado, 0, wx.ALL | wx.CENTER, 5)
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
    self.st_precioAlojamiento.SetLabel('Precio: ' + str(self.listadoRecomendacion[selected].precio))
    self.st_direccionAlojamiento.SetLabel('Dirección: ' + self.listadoRecomendacion[selected].direccion)
    self.st_telefonoAlojamiento.SetLabel('Telefono: ' + str(self.listadoRecomendacion[selected].telefono))
    self.imageBitmap.SetBitmap(wx.BitmapFromImage(self.listadoRecomendacion[selected].imagen))
