from core.model.Cell import Cell

class TableEvaluator():
    def __init__(self) -> None:
        if len(TableEvaluator._memo) == 0:
            TableEvaluator._memo = [-1 for i in range(3**9)]

    # memo is used as static variable to avoid recalculations
    _memo = []

    # player: next to play
    def evaluate(self, table, player) -> int:
        winner = table.getWinner()

        if winner == player:
            return 100
        if winner == Cell.EMPTY:
            return 0
        if winner != None:
            return -100
        
        tableHash = self._hash(table, player)
        if TableEvaluator._memo[tableHash] != -1:
            return TableEvaluator._memo[tableHash]

        # arbitrary low value, so it changes anyway
        bestVal = -200
        otherPlayer = Cell(int(player) ^ 3)
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                if table.getCell(i, j):
                    continue
                table.changeCell(i, j, player)
                # The minus sign assures the algorithm
                # implements a max-min solution
                bestVal = max(bestVal, -self.evaluate(table, otherPlayer))
                # Undo this move to properly iterate
                # through the next possible move
                table.changeCell(i, j, Cell.EMPTY)

        TableEvaluator._memo[tableHash] = bestVal
        return bestVal

    # player: who's turn it is currently
    def _hash(self, table, player) -> int:
        hashVal = 0
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                cell = table.getCell(i,j)
                if cell == Cell.EMPTY:
                    coef = 0
                elif cell == player:
                    coef = 1
                else:
                    coef = 2
                hashVal = 3*hashVal + coef
        return hashVal