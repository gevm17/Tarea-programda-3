from PIL import Image
from xlsxwriter import Workbook
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

imagenes = [
    Image.open(BASE_DIR / "Imagenes" / "alice.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "damir.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "efrem-efre.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "ezgi-kaya.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "i-slam-abruev.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "janvibez.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "jemanuel.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "lorenzo-manera.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "njeromin.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "sergey-antonov.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "share-mashare.jpg"),
    Image.open(BASE_DIR / "Imagenes" / "theerl.jpg")
    ]

for pictures in imagenes:


    alto = 650
    relacion_aspecto = pictures.width / pictures.height
    ancho = int(alto * relacion_aspecto)
    image_resized = pictures.resize((ancho, alto))
    image_resized = image_resized.convert("L")


    marca_agua = Image.open(BASE_DIR / "logo.png").convert("RGBA")
    marca_agua = marca_agua.resize((30, 30))
    image_resized.paste(marca_agua, (image_resized.width - marca_agua.width, image_resized.height - marca_agua.height), marca_agua)

    
    image_resized.save(BASE_DIR / "Imagenes_editadas" / "{}.jpg".format(pictures.filename.split("/")[-1].split(".")[0]))

