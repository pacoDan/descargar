import yt_dlp
import sys

# link = "ingrese link: "
# # url = input(link)
# #
# ydl_opts = {}
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([url])
# print("video descargado satsfactoriamente")
# # print("Ok nos vemos!!")
#

# import sys


def descargar(link):
    print("descargando")
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Descargado!!!")


def procesar_argumentos():
    # Verificar si se proporcionó al menos un argumento
    if len(sys.argv) < 2:
        print("Uso: ./descargar link")
        print("Si no se proporciona el link, se utilizará la carpeta Descargas.")
        return None
    else:
        # El primer argumento es el link
        return sys.argv[1]


if __name__ == "__main__":
    # Procesar los argumentos
    link = procesar_argumentos()

    # Si no se proporcionó un link, usar la carpeta Descargas
    if link is None:
        # Reemplaza "tu_usuario" con tu nombre de usuario de Linux
        link = "/home/daniel_wsl2/Descargas"
    print("El link seleccionado es:", link)
    print("Comenzando a descargar link ->", link)
    descargar(link)

