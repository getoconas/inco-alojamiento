import wx
import src.controller.alojamiento as alojamiento

tmpApp = wx.PySimpleApp()

listadoAlojamiento = []

# TA01
listadoAlojamiento.append(alojamiento.Alojamiento('Eco Cabaña', 'Cabaña', 25000, 'Av. San Martín S/N', 3885108936, wx.Image('img/Cabana/Eco_Cabaña.png'), 'TA01'))
listadoAlojamiento.append(alojamiento.Alojamiento('Mirador del Virrey', 'Cabaña', 25000, 'Ex Ruta 52 - KM 4,4 - Chalala', 3885904057, wx.Image('img/Cabana/Mirador_del_Virrey_Cabaña_Boutique.png'), 'TA01'))
# TA02
listadoAlojamiento.append(alojamiento.Alojamiento('Camping Coquena', 'Camping/Cabaña', 20000, 'Av. San Martín S/N', 3885108936, wx.Image('img/Cabana/Camping_Coquena.png'), 'TA02'))
listadoAlojamiento.append(alojamiento.Alojamiento('Cabañas y Camping Familiar Rodolfo', 'Camping/Cabaña', 15500, 'Ruta 52 S/N', 3884349307, wx.Image('img/Cabana/Mirador_del_Virrey_Cabaña_Boutique.png'), 'TA02'))
listadoAlojamiento.append(alojamiento.Alojamiento('La Posada de Candelaria', 'Hostal', 18000, 'Libertad S/N', 3885879786, wx.Image('img/Hostel/La_Posada_de_la_Candelaria.png'), 'TA02'))
listadoAlojamiento.append(alojamiento.Alojamiento('Pumac', 'Hostal', 25000, 'Pantaleón Cruz S/N', 3885089048, wx.Image('img/Hostel/Pumac.png'), 'TA02'))
# TA03
listadoAlojamiento.append(alojamiento.Alojamiento('Posada El Molle', 'Hostal', 30000, 'Florida 203', 3885043867, wx.Image('img/Hostel/Posada_el_Molle.png'), 'TA03'))
# TA04
listadoAlojamiento.append(alojamiento.Alojamiento('Mama Coca', 'Hostal', 20000, 'Libertad S/N', 3884908434, wx.Image('img/Hostel/MamaCoca.png'), 'TA04'))
listadoAlojamiento.append(alojamiento.Alojamiento('El Rincón del Oso', 'Hostal', 24000, 'Florida 209', 3886049255, wx.Image('img/Hostel/El_Rincon_del_Oso.png'), 'TA04'))
listadoAlojamiento.append(alojamiento.Alojamiento('Pumac', 'Hostal', 25000, 'Pantaleón Cruz S/N', 3885089048, wx.Image('img/Hostel/Pumac.png'), 'TA04'))
listadoAlojamiento.append(alojamiento.Alojamiento('INTI KAY', 'Hostal', 20000, 'Florida esq. Belgrano', 3884076204, wx.Image('img/Hostel/INTI_KAY.png'), 'TA04'))
# TA05
listadoAlojamiento.append(alojamiento.Alojamiento('Mama Coca', 'Hostal', 20000, 'Libertad S/N', 3884908434, wx.Image('img/Hostel/MamaCoca.png'), 'TA05'))
listadoAlojamiento.append(alojamiento.Alojamiento('Doña Velia', 'Hostal', 23000, 'Florida S/N', 3884967488, wx.Image('img/Hostel/Doña_Velia.png'), 'TA05'))
listadoAlojamiento.append(alojamiento.Alojamiento('El Refugio de Noe', 'Hostal', 15000, 'Salta esq Gorriti', 3884803503, wx.Image('img/Hostel/El_Refugio_de_Noe.png'), 'TA05'))
# TA06
listadoAlojamiento.append(alojamiento.Alojamiento('Aguas Coloradas', 'Hostería', 58000, 'Av. San Martín S/N', 3884975583, wx.Image('img/Hosteria/Aguas_Coloradas.png'), 'TA06'))
# TA07
listadoAlojamiento.append(alojamiento.Alojamiento('Nido de Cóndores', 'Hotel', 40000, 'San Ramón Ote 1265', 3885384550, wx.Image('img/Hotel/Nido_de_Condores.png'), 'TA07'))
listadoAlojamiento.append(alojamiento.Alojamiento('La Pushka', 'Hostería', 47000, 'Pasaje Santa Rosa S/N', 3885170350, wx.Image('img/Hosteria/La_Pushka.png'), 'TA07'))
listadoAlojamiento.append(alojamiento.Alojamiento('Wara Wara', 'Hostería', 28000, 'Av. San Martín S/N', 3884780516, wx.Image('img/Hosteria/Wara_Wara.png'), 'TA07'))
# TA08
listadoAlojamiento.append(alojamiento.Alojamiento('Killari', 'Hotel', 50000, 'Sarmineto S/N', 3884908023, wx.Image('img/Hotel/Hotel_Killari.png'), 'TA08'))
# TA09
listadoAlojamiento.append(alojamiento.Alojamiento('Hotel Cactus Cerros', 'Hotel', 42000, 'Av. San Martín S/N', 3884757792, wx.Image('img/Hotel/Hotel_Cactus_Cerro.png'), 'TA09'))
listadoAlojamiento.append(alojamiento.Alojamiento('La Valentina', 'Hotel', 38000, 'Lavalle S/N', 3884560444, wx.Image('img/Hotel/La_Valentina.png'), 'TA09'))
listadoAlojamiento.append(alojamiento.Alojamiento('Las Lavandas Purmamarca', 'Hotel', 52000, 'Av. San Martín 703', 3884103672, wx.Image('img/Hotel/Las_Lavandas_Purmamarca.png'), 'TA09'))
listadoAlojamiento.append(alojamiento.Alojamiento('MAI JAII', 'Hotel', 45000, 'RN52 KM 2', 3884598726, wx.Image('img/Hotel/MAI_JAII.png'), 'TA09'))
listadoAlojamiento.append(alojamiento.Alojamiento('Tierra Virgen Apartaments', 'Hotel', 46000, 'Sarmiento esq. Lavalle', 3884336144, wx.Image('img/Hotel/Tierra_Virgen.png'), 'TA09'))
listadoAlojamiento.append(alojamiento.Alojamiento('Aguas Coloradas', 'Hostería', 58000, 'Av. San Martín S/N', 3884975583, wx.Image('img/Hosteria/Aguas_Coloradas.png'), 'TA09'))
listadoAlojamiento.append(alojamiento.Alojamiento('La Casa Encantanda', 'Hostería', 41000, 'Salta S/N', 3885825305, wx.Image('img/Hosteria/La_Casa_Encantada.png'), 'TA09'))
listadoAlojamiento.append(alojamiento.Alojamiento('La Pushka', 'Hosteria', 47000, 'Pasaje Santa Rosa S/N', 3885170350, wx.Image('img/Hosteria/La_Pushka.png'), 'TA09'))
# TA10
listadoAlojamiento.append(alojamiento.Alojamiento('Nido de Cóndores', 'Hotel', 41000, 'Av. San Martín S/N', 569822092395, wx.Image('img/Hotel/Nido_de_Condores.png'), 'TA10'))
# TA11
listadoAlojamiento.append(alojamiento.Alojamiento('Los Agustinos', 'Hotel', 27000, 'Lavalle S/N', 388505113, wx.Image('img/Hotel/Los_Agustinos.png'), 'TA11'))
listadoAlojamiento.append(alojamiento.Alojamiento('Tierra Virgen Apartaments', 'Hotel', 46000, 'Sarmiento esq. Lavalle', 3884336144, wx.Image('img/Hotel/Tierra_Virgen.png'), 'TA11'))
listadoAlojamiento.append(alojamiento.Alojamiento('Las Vicuñas', 'Hotel', 45000, 'Sarmiento 204', 3884612975, wx.Image('img/Hotel/Las_Vicuñas.png'), 'TA11'))
listadoAlojamiento.append(alojamiento.Alojamiento('El Viejo Algarrobo', 'Hostería', 40000, 'Salta S/N', 3884908286, wx.Image('img/Hosteria/El_Viejo_Algarrobo.png'), 'TA11'))
listadoAlojamiento.append(alojamiento.Alojamiento('Del Amauta', 'Hostería', 42000, 'Salta S/N', 3884908043, wx.Image('img/Hosteria/Del_Amauta.png'), 'TA11'))
# TA12
listadoAlojamiento.append(alojamiento.Alojamiento('Terrazas de la Posta', 'Hostería', 59000, 'Pasaje Santa Rosa S/N', 3884571472, wx.Image('img/Hosteria/Terraza_La_Posta.png'), 'TA12'))
# TA13
listadoAlojamiento.append(alojamiento.Alojamiento('Huara Huasi', 'Hostería', 61000, 'Ex Ruta 52 - KM 5 - Chalala', 3885811804, wx.Image('img/Hosteria/Huara_Huasi.png'), 'TA13'))
# TA14
listadoAlojamiento.append(alojamiento.Alojamiento('Luna Jatun', 'Hotel', 66000, 'Av. San Martín S/N', 3884088669, wx.Image('img/Hotel/Luna_Jatun.png'), 'TA14'))
# TA15
listadoAlojamiento.append(alojamiento.Alojamiento('El Manatial del Silencio', 'Hotel', 99000, 'Av. San Martín S/N', 3884908081, wx.Image('img/Hotel/El_Manantial_del_Silencio.png'), 'TA15'))
listadoAlojamiento.append(alojamiento.Alojamiento('La Comarca', 'Hotel', 79000, 'Ex RN 52 - KM 4.2', 3884908001, wx.Image('img/Hotel/La_Comarca.png'), 'TA15'))
listadoAlojamiento.append(alojamiento.Alojamiento('Marquez de Tojo', 'Hotel', 69000, 'Santa Rosa 4', 3884116001, wx.Image('img/Hotel/Marquez_de_Tojo.png'), 'TA15'))
listadoAlojamiento.append(alojamiento.Alojamiento('Colores de Purmamarca','Hotel', 100000, 'Pasaje Siete Colores S/N', 1155986605, wx.Image('img/Hotel/Colores_de_Purmamarca.png'), 'TA15'))
listadoAlojamiento.append(alojamiento.Alojamiento('El Refugio de Coquena', 'Hotel', 64000, 'Ex RN 52 - KM 3.4', 3884908025, wx.Image('img/Hotel/El_Refugio_de_Coquena.png'), 'TA15'))
# TA16
listadoAlojamiento.append(alojamiento.Alojamiento('Los Colorados Cabañas Botique', 'Cabañas', 75000, 'El Chapacal 511, Paseo de los Colorados', 3884908182, wx.Image('img/Cabana/Los_Colorados.png'), 'TA16'))
listadoAlojamiento.append(alojamiento.Alojamiento('Azul Andino', 'Cabañas', 80000, 'Sarmiento S/N', 1132773021, wx.Image('img/Cabana/Azul_Andino.png'), 'TA16'))
listadoAlojamiento.append(alojamiento.Alojamiento('La Reliquia', 'Hotel', 61000, 'Pantaleon Cruz S/N', 3884908120, wx.Image('img/Hotel/La_Reliquia.png'), 'TA16'))
# TA17
listadoAlojamiento.append(alojamiento.Alojamiento('Luna Jatun', 'Hotel', 66000, 'Av. San Martín S/N', 3884088669, wx.Image('img/Hotel/Luna_Jatun.png'), 'TA17'))
# TA18
listadoAlojamiento.append(alojamiento.Alojamiento('Colores de Purmamarca','Hotel', 100000, 'Pasaje Siete Colores S/N', 1155986605, wx.Image('img/Hotel/Colores_de_Purmamarca.png'), 'TA18'))
listadoAlojamiento.append(alojamiento.Alojamiento('El Cielo de Purmamarca', 'Hotel', 70000, 'Av. San Martín 703', 3884908023, wx.Image('img/Hotel/El_Cielo_de_Purmamarca.png'), 'TA18'))
listadoAlojamiento.append(alojamiento.Alojamiento('Luna Jatun', 'Hotel', 66000, 'Av. San Martín S/N', 3884088669, wx.Image('img/Hotel/Luna_Jatun.png'), 'TA18'))
# TA19
listadoAlojamiento.append(alojamiento.Alojamiento('La Comarca', 'Hotel', 79000, 'Ex RN 52 - KM 4.2', 3884908001, wx.Image('img/Hotel/La_Comarca.png'), 'TA19'))
listadoAlojamiento.append(alojamiento.Alojamiento('Luna Jatun', 'Hotel', 66000, 'Av. San Martín S/N', 3884088669, wx.Image('img/Hotel/Luna_Jatun.png'), 'TA18'))
listadoAlojamiento.append(alojamiento.Alojamiento('Pumahuasi Hotel Boutique', 'Hotel', 64000, 'Av. San Martín S/N', 3885189090, wx.Image('img/Hotel/Pumahuasi_Hotel_Boutique.png'), 'TA19'))

