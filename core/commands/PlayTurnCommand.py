from core.Command import Command
from core.model.Table import table
from core.PlayerManager import playerManager

class PlayTurnCommand(Command):
    def __init__(self, row, col) -> None:
        self._isReduable = True
        self._row = row
        self._col = col
        self._value = playerManager.getCurrentPlayer()
        self._prevValue = table.getCell(row, col)

    def execute(self) -> None:
        table.changeCell(self._row, self._col, self._value)
        self._isExecuted = True

    def undo(self) -> None:
        table.changeCell(self._row, self._col, self._prevValue)
        self._isExecuted = False

    def redo(self) -> None:
        self.execute()