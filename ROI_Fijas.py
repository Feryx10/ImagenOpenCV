import os
import cv2

# Carpeta imágenes positivas
carpeta_positivas = "positivas/"

# Info imágenes positivas
archivo_positivas = "infoPositivas.txt"

# Etiqueta (1 objeto de importancia por imagen)
etiqueta = 1

# Tamaño de la imagen de entrada
tamaño_ventana = (1548, 1548)

# Tamaño de la ROI
tamaño_roi = (65, 65)

def definir_roi(evento, x, y, flags, param):
    global roi
    if evento == cv2.EVENT_LBUTTONDOWN:
        roi = (x - tamaño_roi[0] // 2, y - tamaño_roi[1] // 2, tamaño_roi[0], tamaño_roi[1])
with open(archivo_positivas, "w") as f:
    for imagen in os.listdir(carpeta_positivas):
        if imagen.endswith(".png"):
            ruta_imagen = os.path.join(carpeta_positivas, imagen)
            img = cv2.imread(ruta_imagen)
            img = cv2.resize(img, tamaño_ventana)
            roi = None
            cv2.imshow("Un ROI fija por imagen", img)
            cv2.setMouseCallback("Un ROI fija por imagen", definir_roi)
            while roi is None:
                cv2.waitKey(10)    
            x, y, w, h = roi
            f.write(f"{ruta_imagen} {etiqueta} {x} {y} {w} {h}\n")
            # Dibuja la ROI en la imagen y espera a que el usuario presione ENTER para continuar
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow("ROI seleccionada. Presione ENTER para continuar", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()