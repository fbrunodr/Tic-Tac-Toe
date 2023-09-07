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

    def getCell(self, row, col) -> Cell:
        return self._grid[row][col]

    def changeCell(self, row, col, value) -> None:
        self._grid[row][col] = value
        self.notifyObservers()
    
    def getWinner(self) -> Cell:
        row1 = self._grid[0][0] & self._grid[0][1] & self._grid[0][2]
        if row1 == 1 or row1 == 2:
            return Cell(row1)

        row2 = self._grid[1][0] & self._grid[1][1] & self._grid[1][2]
        if row2 == 1 or row2 == 2:
            return Cell(row2)

        row3 = self._grid[2][0] & self._grid[2][1] & self._grid[2][2]
        if row3 == 1 or row3 == 2:
            return Cell(row3)

        col1 = self._grid[0][0] & self._grid[1][0] & self._grid[2][0]
        if col1 == 1 or col1 == 2:
            return Cell(col1)

        col2 = self._grid[0][1] & self._grid[1][1] & self._grid[2][1]
        if col2 == 1 or col2 == 2:
            return Cell(col2)

        col3 = self._grid[0][2] & self._grid[1][2] & self._grid[2][2]
        if col3 == 1 or col3 == 2:
            return Cell(col3)
        
        main_diag = self._grid[0][0] & self._grid[1][1] & self._grid[2][2]
        if main_diag == 1 or main_diag == 2:
            return Cell(main_diag)

        sec_diag = self._grid[2][0] & self._grid[1][1] & self._grid[0][2]
        if sec_diag == 1 or sec_diag == 2:
            return Cell(sec_diag)

        # Draw
        if all(all([cell != Cell.EMPTY for cell in row]) for row in self._grid):
            return Cell.EMPTY

        # No winner
        return None

## Don't instantiate other tables, pls
table = _Table()