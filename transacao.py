from abc import ABC, abstractmethod

class Transacao(ABC):
    @classmethod
    @abstractmethod
    def registrar(conta):
        pass
