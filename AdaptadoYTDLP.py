from IDescargadorAdapter import IDescargadorAdapter
import yt_dlp

# def descargar2(link):
#     # YouTube(link).streams.first().download()
#     yt = YouTube(link)
#     print("descargando -> " + yt.title)
#     yt.streams.filter(progressive=True, file_extension="mp4").order_by(
#         "resolution"
#     ).desc().first().download()


class AdaptadoYTDLP(IDescargadorAdapter):
    def __init__(self):
        self.link = None

    def descargarReal(self, link: str):  # Agregar 'self' como primer argumento
        print("Descargando...")
        ydl_opts = {
            # Seleccionar la mejor calidad de video y audio
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",  # Formato de salida
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Descargado!!!")

    def descargar(self, url: str):
        self.link = url
        print("Iniciando descarga en AdaptadoYTDLP de Daniel...")
        self.descargarReal(url)
        print("Saliendo de AdaptadoYTDLP de Daniel.")
