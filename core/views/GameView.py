from core.Observer import Observer
from core.model.Cell import Cell
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

    def update(self) -> None:
        return self.show()

    def show(self) -> None:
        self.clearWindow()
        line = ["" for i in range(3)]
        line[2] = str(table.getCell(2,0)) + '|' + str(table.getCell(2,1)) + '|' + str(table.getCell(2,2))
        line[1] = str(table.getCell(1,0)) + '|' + str(table.getCell(1,1)) + '|' + str(table.getCell(1,2))
        line[0] = str(table.getCell(0,0)) + '|' + str(table.getCell(0,1)) + '|' + str(table.getCell(0,2))
        divisor = '-----'
        footer = '0 1 2'

        print('2 ' + line[2])
        print('  ' + divisor)
        print('1 ' + line[1])
        print('  ' + divisor)
        print('0 ' + line[0])
        print('  ' + footer)
        print()

        if table.getWinner() != None:
            self._state = GameState.FINISHED

    def move(self, row, col) -> None:
        gameManager.executeCommand(PlayTurnCommand(row, col))

    @abstractmethod
    def undoMove(self) -> None:
        pass

    @abstractmethod
    def redoMove(self) -> None:
        pass

    def processInput(self) -> None:
        userInput = input('Choose your move (ex.: "1 0", "undo", "redo", "exit"): ')

        if userInput == "undo":
            self.undoMove()
            return self.processInput()
        elif userInput == "redo":
            self.redoMove()
            return self.processInput()
        elif userInput == "exit":
            self._state = GameState.FINISHED
            return

        try:
            row, col = map(int, userInput.split())
        except:
            print("Invalid input")
            return self.processInput()

        validCellResponse = self.validCell(row, col)
        if validCellResponse != "OK":
            print(validCellResponse)
            return self.processInput()

        return self.move(row, col)

    def validCell(self, row, col) -> str:
        if row < 0 or row > 2 or col < 0 or col > 2:
            return "Invalid coordinates;"
        if table.getCell(row, col):
            return "Cell already taken."
        return "OK"