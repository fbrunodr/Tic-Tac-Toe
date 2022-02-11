from core.model.Cell import Cell
from core.views.GameView import GameView
from core.GameManager import gameManager
from core.views.GameState import GameState
from core.model.Table import table
from core.Settings import settings
from core.ai.AIplayer import AIplayer

class GameViewOnePlayer(GameView):
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
        winner = table.getWinner()
        if winner == None:
            return
        elif winner == Cell.EMPTY:
            print("Draw!!!")
            print("Press Enter to continue")
            userInput = input()
            return
        
        AIplayer = settings.getFirstToPlay()
        if not settings.AIplayFirst():
            AIplayer = Cell(int(AIplayer)%2 + 1)
        
        if winner == AIplayer:
            print("You lost :'(")
            print("Better luck next time")
            print("Press Enter to continue")
            userInput = input()
            return
        else:
            print("You WON!!!")
            print("Congratulations!!!")
            print("Press Enter to continue")
            userInput = input()
            return