import os
import cv2

# Ruta de la carpeta con las imágenes positivas
carpeta_positivas = "positivas/"

# Archivo de salida para la lista de imágenes positivas
archivo_positivas = "infoVariasPositivas.txt"

# Tamaño de imagen
tamaño_ventana = (1548, 1548)

# Tamaño de la ROI
tamaño_roi = (65, 65)

def definir_roi(evento, x, y, flags, param):
    global rois
    if evento == cv2.EVENT_LBUTTONDOWN:
        rois.append((x - tamaño_roi[0] // 2, y - tamaño_roi[1] // 2, tamaño_roi[0], tamaño_roi[1]))
with open(archivo_positivas, "w") as f:
    for imagen in os.listdir(carpeta_positivas):
        if imagen.endswith(".png"):
            ruta_imagen = os.path.join(carpeta_positivas, imagen)
            img = cv2.imread(ruta_imagen)
            img = cv2.resize(img, tamaño_ventana)
            rois = []
            cv2.imshow("Varias ROI (presione 'q' para terminar)", img)
            cv2.setMouseCallback("Varias ROI (presione 'q' para terminar)", definir_roi)
            while True:
                cv2.imshow("Varias ROI (presione 'q' para terminar)", img)
                for roi in rois:
                    x, y, w, h = roi
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                key = cv2.waitKey(10) & 0xFF
                if key == ord('q'):
                    break
            etiqueta = len(rois)
            informacion = f"{ruta_imagen} {etiqueta}"
            for roi in rois:
                x, y, w, h = roi
                informacion += f" {x} {y} {w} {h}"
            f.write(informacion + "\n")
            cv2.destroyAllWindows()