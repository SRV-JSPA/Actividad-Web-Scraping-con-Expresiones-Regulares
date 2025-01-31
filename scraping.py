import re
import csv

CENTINELA = None

def cargar_html(archivo, tamano_buffer=1024):
    with open(archivo, 'r', encoding="utf-8") as f:
        while True:
            buffer = f.read(tamano_buffer)

            if not buffer:
                yield CENTINELA
                break
            
            yield buffer

def extraer_productos(trozos_html):
    regex_nombre = r'<h2 [^>]*aria-label="([^"]+)"[^>]*>.*?</h2>'
    regex_imagen = r'<img [^>]*class="s-image"[^>]*src="([^"]+)"'
    
    nombres = []
    imagenes = []
    
    for trozo in trozos_html:
        if trozo == CENTINELA:
            break  
        
        nombres.extend(re.findall(regex_nombre, trozo))
        imagenes.extend(re.findall(regex_imagen, trozo))
    
    return zip(nombres, imagenes)

def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, 'w', newline='', encoding="utf-8") as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(["Nombre del producto", "URL de la imagen"])
        escritor.writerows(productos)

trozos_html = cargar_html("amazon.html", tamano_buffer=1024)

productos = extraer_productos(trozos_html)

exportar_csv(productos, "salida.csv")