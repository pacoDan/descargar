from abc import ABC, abstractmethod
class IDescargadorAdapter(ABC):
    @abstractmethod
    def descargar(self, url: str):
        """IDescargadorAdapter -> Método para descargar contenido desde una URL"""
        pass