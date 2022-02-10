from core.views.GameViewTerminal import GameViewTerminal
from core.GameManager import gameManager
from core.views.GameState import GameState
from core.model.Table import table
from core.Settings import settings
from core.ai.AIplayer import AIplayer

class GameViewTerminalOnePlayer(GameViewTerminal):
    def __init__(self) -> None:
        super().__init__()
        AI = AIplayer()
        table.addObserver(AI)

        player = self
        if settings.AIplayFirst():
            player = AI

        while self._state == GameState.PLAYING:
            player.getUserInput()
            if player == self:
                player = AI
            else:
                player = self

        table.deleteObserver(self)
        table.deleteObserver(AI)
        return self.finish()

    def undoMove(self) -> None:
        gameManager.undo()
        gameManager.undo()

    def redoMove(self) -> None:
        gameManager.redo()
        gameManager.redo()

    def finish(self) -> None:
        pass