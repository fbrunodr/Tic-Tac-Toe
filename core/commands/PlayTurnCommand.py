from core.Command import Command
from core.model.Table import table
from core.PlayerManager import playerManager

class PlayTurnCommand(Command):
    def __init__(self, pos) -> None:
        self._isReduable = True
        self._pos = pos
        self._value = playerManager.getCurrentPlayer()
        self._prevValue = table.getCell(pos)

    def execute(self) -> None:
        table.changeCell(self._pos, self._value)
        self._isExecuted = True

    def undo(self) -> None:
        table.changeCell(self._pos, self._prevValue)
        self._isExecuted = False

    def redo(self) -> None:
        self.execute()