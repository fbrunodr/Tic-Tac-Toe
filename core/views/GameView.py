from core.Observer import Observer
from core.model.Table import table
from core.GameManager import gameManager
from core.commands.ChangeCellCommand import ChangeCellCommand
from core.views.GameState import GameState
from abc import abstractmethod

class GameView(Observer):
    _state = GameState.NOT_STARTED

    def __init__(self) -> None:
        table.addObserver(self)
        table.clear()
        gameManager.clear()
        self._state = GameState.PLAYING

    def getState(self) -> GameState:
        self._state

    def play(self, pos, turn) -> None:
        gameManager.executeCommand(ChangeCellCommand(pos, turn))

    @abstractmethod
    def undoMove(self) -> None:
        pass

    @abstractmethod
    def redoMove(self) -> None:
        pass

    # returns a pair [x, y]
    @abstractmethod
    def getUserInput(self):
        pass