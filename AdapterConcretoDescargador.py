from AdaptadoYTDLP import AdaptadoYTDLP
from IDescargadorAdapter import IDescargadorAdapter

class AdapterConcretoDescargador(IDescargadorAdapter):
    def __init__(self):
        # Crear internamente la instancia de AdaptadoYTDLP
        self.descargador = AdaptadoYTDLP()

    def descargar(self, url: str):
        print("Iniciando descarga en AdapterConcretoDescargador de Daniel...")
        # Delegar la llamada al método descargar de AdaptadoYTDLP
        self.descargador.descargarReal(url)
        print("Saliendo de AdapterConcretoDescargador de Daniel.")
