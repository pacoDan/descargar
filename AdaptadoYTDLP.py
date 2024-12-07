from IDescargadorAdapter import IDescargadorAdapter
import yt_dlp

class AdaptadoYTDLP(IDescargadorAdapter):
    def __init__(self):
        self.link = None

    def descargarReal(self, link: str):  # Agregar 'self' como primer argumento
        print("Iniciando en #AdaptadoYTDLP>>descargarReal()...")
        ydl_opts = {
            # Seleccionar la mejor calidad de video y audio
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",  # Formato de salida
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Saliendo de #AdaptadoYTDLP>>descargarReal()...")

    def descargar(self, url: str):
        self.link = url
        print("Iniciando en #AdaptadoYTDLP>>descargar() de Daniel...")
        self.descargarReal(url)
        print("Saliendo de #AdaptadoYTDLP>>descargar() de Daniel.")