import sys
from AdapterConcretoDescargador import AdapterConcretoDescargador


class Principal:
    def __init__(self, descargador: AdapterConcretoDescargador):
        # self.link = None
        self.descargador = descargador  # Se inyecta una implementación del AdapterConcretoDescargador
        # self.link=self.procesar_argumentos()

    def procesar_argumentos(self):
        # Verificar si se proporcionó al menos un argumento
        if len(sys.argv) < 2:
            print("Uso: python principal.py <link>")
            sys.exit(1)  # Termina el programa si no hay argumentos
        else:
            # El primer argumento es el link
            return sys.argv[1]

    def ejecutar_descarga(self,link :str):
        # Procesar los argumentos
        # link = self.procesar_argumentos()
        print("Iniciando descarga en #Principal>>ejecutar_descarga()...")
        self.descargador.descargar(link)  # Llama al método de descargador


if __name__ == "__main__":
    # Crear la instancia del adaptador
    adaptador = AdapterConcretoDescargador()
    # Crear la instancia de Principal, inyectando el adaptador
    principal = Principal(adaptador)

    # Ejecutar la descarga
    _link=principal.procesar_argumentos()
    print("link obtenido descargando -> "+ _link)
    principal.ejecutar_descarga(_link)
    print("Saliendo del programa principal chauu ...")
