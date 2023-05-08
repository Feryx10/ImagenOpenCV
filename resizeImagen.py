from PIL import Image
import os

# Directorio de entrada
input_dir = "C:\\Users\\input\\"

# Directorio de salida
output_dir = "C:\\Users\\output\\"

# Tamaño deseado para las imágenes
new_size = (1548, 1548)

for filename in os.listdir(input_dir):  
    input_path = os.path.join(input_dir, filename)
    if not os.path.isfile(input_path) or not filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        continue
    with Image.open(input_path) as img:
        img = img.resize(new_size)
        output_path = os.path.join(output_dir, filename)
        img.save(output_path)