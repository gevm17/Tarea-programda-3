from PIL import Image
from xlsxwriter import Workbook


imagenes = [
    Image.open("Imagenes/alice.jpg"),
    Image.open("Imagenes/damir.jpg"),
    Image.open("Imagenes/efrem-efre.jpg"),
    Image.open("Imagenes/ezgi-kaya.jpg"),
    Image.open("Imagenes/i-slam-abruev.jpg"),
    Image.open("Imagenes/janvibez.jpg"),
    Image.open("Imagenes/jemanuel.jpg"),
    Image.open("Imagenes/lorenzo-manera.jpg"),
    Image.open("Imagenes/njeromin.jpg"),
    Image.open("Imagenes/sergey-antonov.jpg"),
    Image.open("Imagenes/share-mashare.jpg"),
    Image.open("Imagenes/theerl.jpg")
    ]

for pictures in imagenes:


    alto = 650
    relacion_aspecto = pictures.width / pictures.height
    ancho = int(alto * relacion_aspecto)
    image_resized = pictures.resize((ancho, alto))
    image_resized = image_resized.convert("L")


    marca_agua = Image.open("logo.png").convert("RGBA")
    marca_agua = marca_agua.resize((30, 30))
    image_resized.paste(marca_agua, (image_resized.width - marca_agua.width, image_resized.height - marca_agua.height), marca_agua)

    
    image_resized.save("Imagenes_editadas/{}.jpg".format(pictures.filename.split("/")[-1].split(".")[0]))

