from pytube import YouTube
import sys


def descargar_subtitulos(link):
    try:
        # Crear objeto YouTube
        yt = YouTube(link)

        # Mostrar información del video
        print(f"Descargando subtítulos para: {yt.title}")

        # Descargar subtítulos en español
        if "es" in yt.captions:
            caption = yt.captions["es"]
            srt_file = f"{yt.title}.es.srt"
            with open(srt_file, "w", encoding="utf-8") as f:
                f.write(caption.generate_srt_captions())
            print(f"Subtítulos en español descargados como: {srt_file}")
        else:
            print("No se encontraron subtítulos en español para este video.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")


def procesar_argumentos():
    if len(sys.argv) < 2:
        print("Uso: python descargar.py <link>")
        return None
    else:
        return sys.argv[1]


if __name__ == "__main__":
    link = procesar_argumentos()
    if link:
        descargar_subtitulos(link)
