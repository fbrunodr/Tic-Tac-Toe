from core.views.GameViewTerminal import GameViewTerminal
from core.GameManager import gameManager
from core.views.GameState import GameState
from core.model.Table import table

class GameViewTerminalTwoPlayers(GameViewTerminal):
    def __init__(self) -> None:
        super().__init__()
        while self._state == GameState.PLAYING:
            self.play()
        table.deleteObserver(self)

    def undoMove(self) -> None:
        gameManager.undo()

    def redoMove(self) -> None:
        gameManager.redo()