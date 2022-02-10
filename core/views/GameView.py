from core.Observer import Observer
from core.model.Table import table
from core.GameManager import gameManager
from core.commands.PlayTurnCommand import PlayTurnCommand
from core.views.GameState import GameState
from abc import abstractmethod

class GameView(Observer):
    def __init__(self) -> None:
        table.addObserver(self)
        table.clear()
        gameManager.clear()
        self._state = GameState.PLAYING

    def getState(self) -> GameState:
        self._state

    @abstractmethod
    def play(self) -> None:
        pass

    def move(self, pos) -> None:
        gameManager.executeCommand(PlayTurnCommand(pos))

    @abstractmethod
    def undoMove(self) -> None:
        pass

    @abstractmethod
    def redoMove(self) -> None:
        pass