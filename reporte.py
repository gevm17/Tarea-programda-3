from xlsxwriter import Workbook
from editor import imagenes

workbook = Workbook("detalle_imagenes.xlsx")
worksheet = workbook.add_worksheet()


libro = Workbook("detalle_imagenes.xlsx")
hoja1 = libro.add_worksheet()
hoja1.write("A1", "Nombre del archivo original", libro.add_format({'bold': True}))
hoja1.write("B1", "Formato de la imagen", libro.add_format({'bold': True}))
hoja1.write("C1", "Ancho original", libro.add_format({'bold': True}))
hoja1.write("D1", "Alto original", libro.add_format({'bold': True}))
hoja1.write("E1", "Estado", libro.add_format({'bold': True}))

for index, pictures in enumerate(imagenes, start=2):
    hoja1.write("A{}".format(index), pictures.filename.split("/")[-1])
    hoja1.write("B{}".format(index), pictures.format)
    hoja1.write("C{}".format(index), pictures.width)
    hoja1.write("D{}".format(index), pictures.height)
    hoja1.write("E{}".format(index), "Procesada")

libro.close()