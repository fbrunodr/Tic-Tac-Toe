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

    def processInput(self) -> None:
        tableEvaluator = TableEvaluator()
        currPlayer = playerManager.getCurrentPlayer()
        otherPlayer = Cell(int(currPlayer) ^ 3)
        bestMoveVal =  tableEvaluator.evaluate(self._proxyTable, currPlayer)
        bestMoves = []
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                if self._proxyTable.getCell(i, j):
                    continue
                self._proxyTable.changeCell(i, j, currPlayer)
                if -tableEvaluator.evaluate(self._proxyTable, otherPlayer) == bestMoveVal:
                    bestMoves.append((i,j))
                self._proxyTable.changeCell(i, j, Cell.EMPTY)

        row, col = random.choice(bestMoves)
        self.move(row, col)

    def move(self, row, col) -> None:
        gameManager.executeCommand(PlayTurnCommand(row, col))