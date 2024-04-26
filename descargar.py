import yt_dlp

link = "ingrese link: "
url = input(link)

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("video descargado satsfactoriamente")
print("Ok nos vemos!!")


# import sys

# def procesar_argumentos():
#     # Verificar si se proporcionó al menos un argumento
#     if len(sys.argv) < 2:
#         print("Uso: ./miprograma <directorio>")
#         print("Si no se proporciona el directorio, se utilizará la carpeta Descargas.")
#         return None
#     else:
#         # El primer argumento es el directorio
#         return sys.argv[1]

# if __name__ == "__main__":
#     # Procesar los argumentos
#     directorio = procesar_argumentos()

#     # Si no se proporcionó un directorio, usar la carpeta Descargas
#     if directorio is None:
#         directorio = "/home/tu_usuario/Descargas"  # Reemplaza "tu_usuario" con tu nombre de usuario de Linux

#     print("El directorio seleccionado es:", directorio)