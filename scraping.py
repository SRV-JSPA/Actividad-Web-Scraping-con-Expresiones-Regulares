import re
import csv

def cargar_html(archivo):
    with open(archivo, 'r', encoding="utf-8") as f:
        return f.read()
    
def extraer_productos(html):
    regex_nombre = r'<h2 [^>]*aria-label="([^"]+)"[^>]*>.*?</h2>'
    regex_imagen = r'<img [^>]*class="s-image"[^>]*src="([^"]+)"'
    nombres = re.findall(regex_nombre, html)
    imagenes = re.findall(regex_imagen, html)
    return zip(nombres, imagenes)

def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre del producto", "URL de la imagen"])
        writer.writerows(productos)
        
html = cargar_html("amazon.html")
productos = extraer_productos(html)

exportar_csv(productos, "salida.csv")