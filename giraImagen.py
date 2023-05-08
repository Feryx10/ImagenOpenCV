from PIL import Image
import os

# Ruta origen
ruta_origen = "C:\\Users\\"

# Ruta destino
ruta_destino = "C:\\Users\\"

# Grados a girar
grados = 90

# Lista de todas las imágenes 
archivos = os.listdir(ruta_origen)

for archivo in archivos: 
    ruta_completa_origen = os.path.join(ruta_origen, archivo)
    imagen = Image.open(ruta_completa_origen)
    imagen_girada = imagen.rotate(grados, expand=True).convert("RGBA") 
    nombre_archivo_sin_extension = os.path.splitext(archivo)[0]
    nombre_archivo_destino = nombre_archivo_sin_extension + ".png"
    ruta_completa_destino = os.path.join(ruta_destino, nombre_archivo_destino)
    imagen_girada.save(ruta_completa_destino)