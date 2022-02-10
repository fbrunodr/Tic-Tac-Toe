import random
from copy import deepcopy
from core.Observer import Observer
from core.model.Cell import Cell
from core.model.Table import table
from core.PlayerManager import playerManager
from core.ai.TableEvaluator import TableEvaluator
from core.GameManager import gameManager
from core.commands.PlayTurnCommand import PlayTurnCommand

class AIplayer(Observer):
    def __init__(self) -> None:
        self._proxyTable = deepcopy(table)
        self._proxyTable.clearObservers()

    def update(self) -> None:
        self._proxyTable = deepcopy(table)
        self._proxyTable.clearObservers()

    def getUserInput(self) -> None:
        tableEvaluator = TableEvaluator()
        currPlayer = playerManager.getCurrentPlayer()
        otherPlayer = Cell(int(currPlayer)%2 + 1)
        bestMoveVal =  tableEvaluator.evaluate(self._proxyTable, currPlayer, currPlayer)
        bestMoves = []
        for i in range(3):
            for j in range(3):
                if self._proxyTable.getCell([i,j]) != Cell.EMPTY:
                    continue
                self._proxyTable.changeCell([i,j], currPlayer)
                if tableEvaluator.evaluate(self._proxyTable, currPlayer, otherPlayer) == bestMoveVal:
                    bestMoves.append([i,j])
                self._proxyTable.changeCell([i,j], Cell.EMPTY)

        self.move(random.choice(bestMoves))

    def move(self, pos) -> None:
        gameManager.executeCommand(PlayTurnCommand(pos))