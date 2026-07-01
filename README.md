Editor de Imágenes y Generador de Reportes
Descripción

Este proyecto automatiza el procesamiento de imágenes mediante Python. El programa realiza las siguientes tareas:

Carga imágenes desde una carpeta local.
Redimensiona las imágenes manteniendo su proporción.
Convierte las imágenes a escala de grises.
Agrega una marca de agua en la esquina inferior derecha.
Guarda las imágenes procesadas en una carpeta de salida.
Genera un reporte en formato Excel con información de cada imagen procesada.
Estructura del Proyecto
Proyecto/
│
├── main.py
├── editor.py
├── reporte.py
├── logo.png
│
├── Imagenes/
│   ├── alice.jpg
│   ├── damir.jpg
│   ├── ...
│
├── Imagenes_editadas/
│
└── detalle_imagenes.xlsx
Requisitos
Python

Se recomienda utilizar Python 3.8 o superior.

Dependencias

Instalar las bibliotecas necesarias:

pip install pillow xlsxwriter
Funcionamiento
1. Procesamiento de imágenes

El módulo editor.py realiza las siguientes operaciones sobre cada imagen:

Carga la imagen original.
Ajusta la altura a 650 píxeles.
Calcula automáticamente el ancho para conservar la relación de aspecto.
Convierte la imagen a escala de grises.
Inserta una marca de agua utilizando el archivo logo.png.
Guarda la imagen procesada en la carpeta Imagenes_editadas.
2. Generación del reporte

El módulo reporte.py crea un archivo Excel llamado:

detalle_imagenes.xlsx

El reporte incluye:

Columna	Descripción
Nombre de la imagen	Nombre del archivo
Formato de la imagen	Tipo de formato (JPEG, PNG, etc.)
Ancho original	Ancho en píxeles
Alto original	Alto en píxeles
Estado	Estado del procesamiento
3. Ejecución

Para ejecutar el programa:

python main.py

Salida esperada:

¡Bienvenido al programa de edición de imágenes!
Las imágenes han sido procesadas y el reporte ha sido generado.
Tecnologías Utilizadas
Python
Pillow (PIL)
XlsxWriter
Características

✔ Redimensionamiento automático.

✔ Conversión a escala de grises.

✔ Inserción de marca de agua.

✔ Generación automática de reportes Excel.

✔ Procesamiento por lotes de múltiples imágenes.

Mejoras Futuras
Manejo de errores para imágenes inexistentes.
Soporte para formatos PNG y WebP.
Configuración dinámica del tamaño de la marca de agua.
Selección de carpetas mediante interfaz gráfica.
Registro de actividades mediante archivos de log.
Autor

Proyecto desarrollado como práctica de automatización y procesamiento de imágenes con Python.