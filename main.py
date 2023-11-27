import wx

import src.view.mainWindow as alojamiento
    
# Definición principal de la aplicación
if __name__ == '__main__':
  app = wx.App()
  app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
  frame = alojamiento.MainWindow()
  frame.Show()
  app.MainLoop()

# TOCONAS, GASTON ENZO - GRUPO 10 - INCO
