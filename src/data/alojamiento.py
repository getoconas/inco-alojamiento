import wx
import src.controller.alojamiento as alojamiento

tmpApp = wx.PySimpleApp()

# Definicion de rutas de las imagenes
IMAGENES = {
  'Aguas Coloradas': 'img/Hosteria/Aguas_Coloradas.png',
  'Azul Andino': 'img/Cabana/Azul_Andino.png',
  'Cabañas y Camping Familiar Rodolfo': 'img/Cabana/Mirador_del_Virrey_Cabaña_Boutique.png',
  'Camping Coquena': 'img/Cabana/Camping_Coquena.png',
  'Colores de Purmamarca': 'img/Hotel/Colores_de_Purmamarca.png',
  'Del Amauta': 'img/Hosteria/Del_Amauta.png',
  'Doña Velia': 'img/Hostel/Doña_Velia.png',
  'Eco Cabaña': 'img/Cabana/Eco_Cabaña.png',
  'El Cielo de Purmamarca': 'img/Hotel/El_Cielo_de_Purmamarca.png',
  'El Manatial del Silencio': 'img/Hotel/El_Manantial_del_Silencio.png',
  'El Refugio de Coquena': 'img/Hotel/El_Refugio_de_Coquena.png',
  'El Refugio de Noe': 'img/Hostel/El_Refugio_de_Noe.png',
  'El Rincón del Oso': 'img/Hostel/El_Rincon_del_Oso.png',
  'El Viejo Algarrobo': 'img/Hosteria/El_Viejo_Algarrobo.png',
  'Hotel Cactus Cerros': 'img/Hotel/Hotel_Cactus_Cerro.png',
  'Huara Huasi': 'img/Hosteria/Huara_Huasi.png',
  'INTI KAY': 'img/Hostel/INTI_KAY.png',
  'Killari': 'img/Hotel/Hotel_Killari.png',
  'La Casa Encantanda': 'img/Hosteria/La_Casa_Encantada.png',
  'La Comarca': 'img/Hotel/La_Comarca.png',
  'La Posada de Candelaria': 'img/Hostel/La_Posada_de_la_Candelaria.png',
  'La Pushka': 'img/Hosteria/La_Pushka.png',
  'La Reliquia': 'img/Hotel/La_Reliquia.png',
  'La Valentina': 'img/Hotel/La_Valentina.png',
  'Las Lavandas Purmamarca': 'img/Hotel/Las_Lavandas_Purmamarca.png',
  'Las Vicuñas': 'img/Hotel/Las_Vicuñas.png',
  'Los Colorados Cabañas Botique': 'img/Cabana/Los_Colorados.png',
  'Los Agustinos': 'img/Hotel/Los_Agustinos.png',
  'Luna Jatun': 'img/Hotel/Luna_Jatun.png',
  'MAI JAII': 'img/Hotel/MAI_JAII.png',
  'Mama Coca': 'img/Hostel/MamaCoca.png',
  'Marquez de Tojo': 'img/Hotel/Marquez_de_Tojo.png',
  'Mirador del Virrey': 'img/Cabana/Mirador_del_Virrey_Cabaña_Boutique.png',
  'Nido de Cóndores': 'img/Hotel/Nido_de_Condores.png',
  'Posada El Molle': 'img/Hostel/Posada_el_Molle.png',
  'Pumac': 'img/Hostel/Pumac.png', 
  'Pumahuasi Hotel Boutique': 'img/Hotel/Pumahuasi_Hotel_Boutique.png',
  'Terrazas de la Posta': 'img/Hosteria/Terraza_La_Posta.png',
  'Tierra Virgen Apartaments': 'img/Hotel/Tierra_Virgen.png',
  'Wara Wara': 'img/Hosteria/Wara_Wara.png'
}

# Definicion de datos de alojamientos
datos_alojamientos = [
  # TA01
  ('Eco Cabaña', 'Cabaña', 25000, 'Av. San Martín S/N', 3885108936, 'TA01'),
  ('Mirador del Virrey', 'Cabaña', 25000, 'Ex Ruta 52 - KM 4,4 - Chalala', 3885904057, 'TA01'),
  # TA02
  ('Camping Coquena', 'Camping/Cabaña', 20000, 'Av. San Martín S/N', 3885108936, 'TA02'),
  ('Cabañas y Camping Familiar Rodolfo', 'Camping/Cabaña', 15500, 'Ruta 52 S/N', 3884349307, 'TA02'),
  ('La Posada de Candelaria', 'Hostal', 18000, 'Libertad S/N', 3885879786, 'TA02'),
  ('Pumac', 'Hostal', 25000, 'Pantaleón Cruz S/N', 3885089048, 'TA02'),
  # TA03
  ('Posada El Molle', 'Hostal', 30000, 'Florida 203', 3885043867, 'TA03'),
  # TA04
  ('Mama Coca', 'Hostal', 20000, 'Libertad S/N', 3884908434, 'TA04'),
  ('El Rincón del Oso', 'Hostal', 24000, 'Florida 209', 3886049255, 'TA04'),
  ('Pumac', 'Hostal', 25000, 'Pantaleón Cruz S/N', 3885089048, 'TA04'),
  ('INTI KAY', 'Hostal', 20000, 'Florida esq. Belgrano', 3884076204, 'TA04'),
  # TA05
  ('Mama Coca', 'Hostal', 20000, 'Libertad S/N', 3884908434, 'TA05'),
  ('Doña Velia', 'Hostal', 23000, 'Florida S/N', 3884967488, 'TA05'),
  ('El Refugio de Noe', 'Hostal', 15000, 'Salta esq Gorriti', 3884803503, 'TA05'),
  # TA06
  ('Aguas Coloradas', 'Hostería', 58000, 'Av. San Martín S/N', 3884975583, 'TA06'),
  # TA07
  ('Nido de Cóndores', 'Hotel', 40000, 'San Ramón Ote 1265', 3885384550, 'TA07'),
  ('La Pushka', 'Hostería', 47000, 'Pasaje Santa Rosa S/N', 3885170350, 'TA07'),
  ('Wara Wara', 'Hostería', 28000, 'Av. San Martín S/N', 3884780516, 'TA07'),
  # TA08
  ('Killari', 'Hotel', 50000, 'Sarmineto S/N', 3884908023, 'TA08'),
  # TA09
  ('Hotel Cactus Cerros', 'Hotel', 42000, 'Av. San Martín S/N', 3884757792, 'TA09'),
  ('La Valentina', 'Hotel', 38000, 'Lavalle S/N', 3884560444, 'TA09'),
  ('Las Lavandas Purmamarca', 'Hotel', 52000, 'Av. San Martín 703', 3884103672, 'TA09'),
  ('MAI JAII', 'Hotel', 45000, 'RN52 KM 2', 3884598726, 'TA09'),
  ('Tierra Virgen Apartaments', 'Hotel', 46000, 'Sarmiento esq. Lavalle', 3884336144, 'TA09'),
  ('Aguas Coloradas', 'Hostería', 58000, 'Av. San Martín S/N', 3884975583, 'TA09'),
  ('La Casa Encantanda', 'Hostería', 41000, 'Salta S/N', 3885825305, 'TA09'),
  ('La Pushka', 'Hosteria', 47000, 'Pasaje Santa Rosa S/N', 3885170350, 'TA09'),
  # TA10
  ('Nido de Cóndores', 'Hotel', 41000, 'Av. San Martín S/N', 569822092395, 'TA10'),
  # TA11
  ('Los Agustinos', 'Hotel', 27000, 'Lavalle S/N', 388505113, 'TA11'),
  ('Tierra Virgen Apartaments', 'Hotel', 46000, 'Sarmiento esq. Lavalle', 3884336144, 'TA11'),
  ('Las Vicuñas', 'Hotel', 45000, 'Sarmiento 204', 3884612975, 'TA11'),
  ('El Viejo Algarrobo', 'Hostería', 40000, 'Salta S/N', 3884908286, 'TA11'),
  ('Del Amauta', 'Hostería', 42000, 'Salta S/N', 3884908043, 'TA11'),
  # TA12
  ('Terrazas de la Posta', 'Hostería', 59000, 'Pasaje Santa Rosa S/N', 3884571472, 'TA12'),
  # TA13
  ('Huara Huasi', 'Hostería', 61000, 'Ex Ruta 52 - KM 5 - Chalala', 3885811804, 'TA13'),
  # TA14
  ('Luna Jatun', 'Hotel', 66000, 'Av. San Martín S/N', 3884088669, 'TA14'),
  # TA15
  ('El Manatial del Silencio', 'Hotel', 99000, 'Av. San Martín S/N', 3884908081, 'TA15'),
  ('La Comarca', 'Hotel', 79000, 'Ex RN 52 - KM 4.2', 3884908001, 'TA15'),
  ('Marquez de Tojo', 'Hotel', 69000, 'Santa Rosa 4', 3884116001, 'TA15'),
  ('Colores de Purmamarca','Hotel', 100000, 'Pasaje Siete Colores S/N', 1155986605, 'TA15'),
  ('El Refugio de Coquena', 'Hotel', 64000, 'Ex RN 52 - KM 3.4', 3884908025, 'TA15'),
  # TA16
  ('Los Colorados Cabañas Botique', 'Cabañas', 75000, 'El Chapacal 511, Paseo de los Colorados', 3884908182, 'TA16'),
  ('Azul Andino', 'Cabañas', 80000, 'Sarmiento S/N', 1132773021, 'TA16'),
  ('La Reliquia', 'Hotel', 61000, 'Pantaleon Cruz S/N', 3884908120, 'TA16'),
  # TA17
  ('Luna Jatun', 'Hotel', 66000, 'Av. San Martín S/N', 3884088669, 'TA17'),
  # TA18
  ('Colores de Purmamarca','Hotel', 100000, 'Pasaje Siete Colores S/N', 1155986605, 'TA18'),
  ('El Cielo de Purmamarca', 'Hotel', 70000, 'Av. San Martín 703', 3884908023, 'TA18'),
  ('Luna Jatun', 'Hotel', 66000, 'Av. San Martín S/N', 3884088669, 'TA18'),
  # TA19
  ('La Comarca', 'Hotel', 79000, 'Ex RN 52 - KM 4.2', 3884908001, 'TA19'),
  ('Luna Jatun', 'Hotel', 66000, 'Av. San Martín S/N', 3884088669, 'TA18'),
  ('Pumahuasi Hotel Boutique', 'Hotel', 64000, 'Av. San Martín S/N', 3885189090, 'TA19')
]

# Crear un objeto de tipo alojamiento
def agregar_alojamiento(lista, nombre, categoria, precio, direccion, telefono, tipo):
  imagen = wx.Image(IMAGENES[nombre])
  lista.append(alojamiento.Alojamiento(nombre, categoria, precio, direccion, telefono, imagen, tipo))

# Lista de alojamientos
listadoAlojamiento = []

# Agregar todos los alojamientos al listado
for datos in datos_alojamientos:
  agregar_alojamiento(listadoAlojamiento, *datos)
