from core.Observable import Observable
from core.model.Cell import Cell

# Don't instantiate this class, import the settings object at the bottom
class _Settings(Observable):
    def __init__(self) -> None:
        super().__init__()
        self._firstToPlay = Cell.CROSS
        self._AIstartsGame = False
        self.notifyObservers()

    def setFirstToPlay(self, value) -> None:
        self._firstToPlay = value
        self.notifyObservers()

    def getFirstToPlay(self) -> Cell:
        return self._firstToPlay

    def setAIstarts(self, value) -> None:
        self._AIstartsGame = value
        self.notifyObservers()

    def AIplayFirst(self) -> bool:
        return self._AIstartsGame

## Don't instantiate other settings objects, pls
settings = _Settings()