from core.views.GameState import GameState
from core.views.GameView import GameView
from core.model.Cell import Cell
from core.model.Table import table

class GameViewTerminal(GameView):

    def update(self) -> None:
        return self.show()

    def show(self) -> None:
        self.clearWindow()
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

        if table.getWinner() != None:
            self._state = GameState.FINISHED

    def getUserInput(self) -> None:
        userInput = input('Choose your move (ex.: "1 0", "undo", "redo", "exit"): ')

        if userInput == "undo":
            print()
            self.undoMove()
            return self.getUserInput()
        elif userInput == "redo":
            print()
            self.redoMove()
            return self.getUserInput()
        elif userInput == "exit":
            self._state = GameState.FINISHED
            return

        try:
            x, y = map(int, userInput.split())
        except:
            print("Invalid input")
            return self.getUserInput()

        pos = [x,y]
        validCellResponse = self.validCell(pos)
        if validCellResponse != "OK":
            print(validCellResponse)
            return self.getUserInput()

        print()
        return self.move(pos)

    def validCell(self, pos) -> str:
        x, y = pos
        if x < 0 or x > 2 or y < 0 or y > 2:
            return "Invalid coordinates;"
        if table.getCell([x,y]) != Cell.EMPTY:
            return "Cell already taken."
        return "OK"