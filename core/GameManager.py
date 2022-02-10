from core.PlayerManager import playerManager

# Don't instantiate this class, import the game manager at the bottom
class _GameManager:
    def __init__(self) -> None:
        self._undoStack = []
        self._redoStack = []

    def executeCommand(self, command) -> None:
        self._redoStack.clear()
        command.execute()
        playerManager.changeCurrentPlayer()
        self._undoStack.append(command)

    def undo(self) -> None:
        if len(self._undoStack) == 0:
            return
        self._undoStack[-1].undo()
        playerManager.changeCurrentPlayer()
        self._redoStack.append(self._undoStack[-1])
        self._undoStack.pop()

    def redo(self) -> None:
        if len(self._redoStack) == 0:
            return

        self._redoStack[-1].redo()
        playerManager.changeCurrentPlayer()
        self._undoStack.append(self._redoStack[-1])
        self._redoStack.pop()

    def clear(self) -> None:
        self._undoStack.clear()
        self._redoStack.clear()

## Don't instantiate other game managers, pls
gameManager = _GameManager()