from abc import ABC

class Observable(ABC):
    _observers = []

    def notifyObservers(self) -> None:
        for observer in self._observers:
            observer.update()

    def addObserver(self, observer) -> None:
        self._observers.append(observer)

    def deleteObserver(self, observer) -> None:
        self._observers.remove(observer)