from core.views.GameView import GameView
from core.GameManager import gameManager
from core.views.GameState import GameState
from core.model.Table import table
from core.model.Cell import Cell

class GameViewTwoPlayers(GameView):
    def __init__(self) -> None:
        super().__init__()
        while self._state == GameState.PLAYING:
            self.getUserInput()
        table.deleteObserver(self)
        return self.finish()

    def undoMove(self) -> None:
        gameManager.undo()

    def redoMove(self) -> None:
        gameManager.redo()

    def finish(self) -> None:
        winner = table.getWinner()
        if winner == None:
            return
        elif winner == Cell.EMPTY:
            print("Draw!!!")
            print("Press Enter to continue")
            userInput = input()
            return

        print("Player with " + str(winner) + " wins!!")
        userInput = input("Press Enter to continue")
        return