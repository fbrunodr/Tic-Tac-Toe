from core.model.Cell import Cell
from core.views.GameView import GameView
from core.GameManager import gameManager
from core.PlayerManager import playerManager
from core.views.GameState import GameState
from core.model.Table import table
from core.Settings import settings
from core.ai.AIplayer import AIplayer
# import time

class GameViewOnePlayer(GameView):
    def __init__(self) -> None:
        super().__init__()
        self.AI = AIplayer()
        table.addObserver(self.AI)

        player = self
        if settings.AIplayFirst():
            player = self.AI

        while self._state == GameState.PLAYING:
            # start = time.time()
            player.processInput()
            if player == self:
                player = self.AI
            else:
                player = self
            # end = time.time()
            # print(end - start)

        return self.finish()

    def undoMove(self) -> None:
        if self.firstMove() and settings.AIplayFirst():
            gameManager.undo()
            self.AI.processInput()
            return

        gameManager.undo()
        gameManager.undo()

    def firstMove(self) -> bool:
        currentPlayer = playerManager.getCurrentPlayer()
        for i in range(3):
            for j in range(3):
                if currentPlayer == table.getCell(i,j):
                    return False
        return True

    def redoMove(self) -> None:
        gameManager.redo()
        gameManager.redo()

    def finish(self) -> None:
        table.deleteObserver(self)
        table.deleteObserver(self.AI)
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
            AIplayer = Cell(AIplayer ^ 3)
        
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