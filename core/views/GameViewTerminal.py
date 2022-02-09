from email import header
from core.views.GameState import GameState
from core.views.GameView import GameView
from core.model.Cell import Cell
from core.model.Table import table
from core.GameManager import gameManager

class GameViewTerminal(GameView):
    def __init__(self) -> None:
        super().__init__()
        while self._state == GameState.PLAYING:
            self.getUserInput()
        table.deleteObserver(self)

    def update(self):
        line = ["" for i in range(3)]
        line[2] = str(table.getCell([2,0])) + '|' + str(table.getCell([2,1])) + '|' + str(table.getCell([2,2]))
        line[1] = str(table.getCell([1,0])) + '|' + str(table.getCell([1,1])) + '|' + str(table.getCell([1,2]))
        line[0] = str(table.getCell([0,0])) + '|' + str(table.getCell([0,1])) + '|' + str(table.getCell([0,2]))
        divisor = '-----'
        footer = '0 1 2'

        for i in range(3):
            line[i] = line[i].replace(str(Cell.CROSS), 'X')
            line[i] = line[i].replace(str(Cell.CIRCLE), 'O')
            line[i] = line[i].replace(str(Cell.EMPTY), ' ')

        print('2 ' + line[2])
        print('  ' + divisor)
        print('1 ' + line[1])
        print('  ' + divisor)
        print('0 ' + line[0])
        print('  ' + footer)
        print()

        if table.getWinner() != Cell.EMPTY:
            self._state = GameState.FINISHED

    def undoMove(self) -> None:
        gameManager.undo()

    def redoMove(self) -> None:
        gameManager.redo()

    def getUserInput(self):
        userInput = input('Chosse your move (ex.: "1 0", "undo", "redo"): ')

        if userInput == "undo":
            print()
            self.undoMove()
            return
        elif userInput == "redo":
            print()
            self.redoMove()
            return

        x, y = map(int, userInput.split())
        pos = [x,y]
        validCellResponse = self.validCell(pos)
        if validCellResponse != "OK":
            print(validCellResponse)
            return
        print()
        self.play(pos, Cell.CROSS)

    def validCell(self, pos) -> str:
        x, y = pos
        if x < 0 or x > 2 or y < 0 or y > 2:
            return "Invalid coordinates;"
        if table.getCell([x,y]) != Cell.EMPTY:
            return "Cell already taken."
        return "OK"