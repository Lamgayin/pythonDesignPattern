from abc import ABCMeta,abstractclassmethod
class Observer(metaclass=ABCMeta):
    @abstractclassmethod
    def update(self,observable,object):
        pass
    
class Observable:
    def __init__(self):
        self._observers = []
    def addObservers(self,observer):
        self._observers.append(observer)
    def removeObservers(self,observer):
        self._observers.remove(observer)
    def notifyObservers(self,object=0):
        for o in self._observers:
            o.update(self,object)