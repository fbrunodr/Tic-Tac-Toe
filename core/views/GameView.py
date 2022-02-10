from core.Observer import Observer
from core.model.Table import table
from core.GameManager import gameManager
from core.PlayerManager import playerManager
from core.commands.PlayTurnCommand import PlayTurnCommand
from core.views.GameState import GameState
from core.views.View import View
from abc import abstractmethod

class GameView(View, Observer):
    def __init__(self) -> None:
        table.addObserver(self)
        table.clear()
        gameManager.clear()
        playerManager.clear()
        
        self._state = GameState.PLAYING

    def getState(self) -> GameState:
        self._state

    def move(self, pos) -> None:
        gameManager.executeCommand(PlayTurnCommand(pos))

    @abstractmethod
    def undoMove(self) -> None:
        pass

    @abstractmethod
    def redoMove(self) -> None:
        pass