from abc import abstractmethod
from abc import ABCMeta


class IFicha(metaclass=ABCMeta):

    @abstractmethod
    def add(self):
        
        pass

    @abstractmethod
    def liga(self):
      
        pass

    @abstractmethod
    def enemigo(self):
        
        pass