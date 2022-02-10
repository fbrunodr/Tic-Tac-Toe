from core.model.Cell import Cell

# Don't instantiate this class, import the settings object at the bottom
class _Settings():
    def __init__(self) -> None:
        self._firstToPlay = Cell.CROSS
        self._AIstartsGame = False

    def setFirstToPlay(self, value) -> None:
        self._firstToPlay = value

    def getFirstToPlay(self) -> Cell:
        return self._firstToPlay

    def setAIstarts(self, value) -> None:
        self._AIstartsGame = value

    def AIplayFirst(self) -> bool:
        return self._AIstartsGame

## Don't instantiate other settings objects, pls
settings = _Settings()