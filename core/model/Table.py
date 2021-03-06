from core.model.Cell import Cell
from core.Observable import Observable

# Don't instantiate this class, import the table instance at the bottom
class _Table(Observable):
    def __init__(self) -> None:
        super().__init__()
        self._grid = [ [ Cell.EMPTY for j in range(3) ] for i in range(3) ]

    def clear(self) -> None:
        for i in range(3):
            for j in range(3):
                self._grid[i][j] = Cell.EMPTY
        self.notifyObservers()

    def getCell(self, pos) -> None:
        x, y = pos
        return self._grid[x][y]

    def changeCell(self, pos, value) -> None:
        x, y = pos
        self._grid[x][y] = value
        self.notifyObservers()
    
    def getWinner(self) -> Cell:
        # Rows
        for i in range(3):
            value = self._grid[i][0]
            if value == Cell.EMPTY:
                continue
            row = self._grid[i]
            if all(cell == value for cell in row):
                return value

        # Collumns
        for j in range(3):
            value = self._grid[0][j]
            if value == Cell.EMPTY:
                continue
            collumn = [row[j] for row in self._grid]
            if all(cell == value for cell in collumn):
                return value

        # Diagonals
        mainDiagonal = [self._grid[i][i] for i in range(3)]
        value = mainDiagonal[0]
        if value != Cell.EMPTY and all(cell == value for cell in mainDiagonal):
            return value

        secondaryDiagonal = [self._grid[i][2-i] for i in range(3)]
        value = secondaryDiagonal[0]
        if value != Cell.EMPTY and all(cell == value for cell in secondaryDiagonal):
            return value
        
        # Draw
        if all(all([cell != Cell.EMPTY for cell in row]) for row in self._grid):
            return Cell.EMPTY

        # No winner
        return None

## Don't instantiate other tables, pls
table = _Table()