import yt_dlp
import sys
import os


def descargar(link):
    print("Descargando...")
    ydl_opts = {
        # Seleccionar la mejor calidad de video y audio
        "format": "bestvideo+bestaudio/best",
        # "merge_output_format": "mp4",  # Formato de salida
        "outtmpl": "%(title)s.%(ext)s",  # Formato del nombre del archivo
        "writesubtitles": True,  # Descargar subtítulos
        "subtitleslangs": ["es-orig"],  # Idiomas de los subtítulos (puedes agregar más)
        "skip_download": False,  # Asegúrate de que se descargue el video
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Descargado!!!")

    # # Convertir subtítulos a .txt
    # for lang in ["es"]:  # Idiomas de los subtítulos
    #     srt_file = f"{ydl.prepare_filename(ydl.extract_info(link))}.{lang}.srt"
    #     txt_file = f"{ydl.prepare_filename(ydl.extract_info(link))}.{lang}.txt"
    #
    #     # Verificar si el archivo .srt existe antes de intentar abrirlo
    #     if os.path.exists(srt_file):
    #         with (
    #             open(srt_file, "r", encoding="utf-8") as srt,
    #             open(txt_file, "w", encoding="utf-8") as txt,
    #         ):
    #             for line in srt:
    #                 # Escribir solo las líneas de texto en el archivo .txt
    #                 if (
    #                     not line.startswith(
    #                         ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    #                     )
    #                     and line.strip()
    #                 ):
    #                     txt.write(line)
    #         print(f"Subtítulos convertidos a {txt_file}")
    #     else:
    #         print(f"No se encontraron subtítulos en {lang} para el video.")


# def descargar2(link):
#     # YouTube(link).streams.first().download()
# yt = YouTube(link)
# print("descargando -> " + yt.title)
# yt.streams.filter(progressive=True, file_extension="mp4").order_by(
#     "resolution"
# ).desc().first().download()


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
