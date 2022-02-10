from core.model.Cell import Cell
from core.Settings import settings

# Don't instantiate this class, import the object at the bottom
class _PlayerManager():
    def __init__(self) -> None:
        self._currentPlayer = settings.getFirstToPlay()

    def clear(self) -> None:
        return self.__init__()

    def getCurrentPlayer(self) -> Cell:
        return self._currentPlayer

    def changeCurrentPlayer(self) -> None:
        self._currentPlayer = Cell(int(self._currentPlayer)%2 + 1)

playerManager = _PlayerManager()