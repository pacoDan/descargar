import requests
from bs4 import BeautifulSoup
import re
import sys


def obtener_subtitulos(video_id):
    # URL del video
    url = f"https://www.youtube.com/watch?v={video_id}"

    # Hacer una solicitud a la página del video
    response = requests.get(url)
    if response.status_code != 200:
        print("Error al acceder al video.")
        return None

    # Analizar el contenido de la página
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar el script que contiene los subtítulos
    scripts = soup.find_all("script")
    for script in scripts:
        if "ytplayer.config" in script.text:
            # Extraer el contenido del script
            config_text = script.string
            break
    else:
        print("No se encontraron subtítulos.")
        return None

    # Buscar el enlace de los subtítulos
    match = re.search(r'"captions":\s*({.*?})', config_text)
    if match:
        captions_data = match.group(1)
        print("Subtítulos encontrados:", captions_data)
        return captions_data
    else:
        print("No se encontraron subtítulos.")
        return None


def procesar_argumentos():
    if len(sys.argv) < 2:
        print("Uso: python descargar.py <link>")
        return None
    else:
        return sys.argv[1]


if __name__ == "__main__":
    link = procesar_argumentos()
    if link:
        video_id = link.split("v=")[-1]
        obtener_subtitulos(video_id)
