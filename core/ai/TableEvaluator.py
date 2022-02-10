from core.model.Cell import Cell

class TableEvaluator():
    # memo is used as static variable to avoid recalculations
    _memo = {}

    # player: the player interested on the evaluation
    # turn: who's turn it is currently
    def evaluate(self, table, player, turn) -> int:
        if table.getWinner() == player:
            return 100
        if table.getWinner() == Cell.EMPTY:
            return 0
        if table.getWinner() != None:
            return -100
        
        tableHash = self._hash(table, player, turn)
        if tableHash in TableEvaluator._memo:
            return TableEvaluator._memo[tableHash]

        # arbitrary low value, so it changes anyway
        bestVal = -200
        for i in range(3):
            for j in range(3):
                if table.getCell([i,j]) != Cell.EMPTY:
                    continue
                table.changeCell([i,j], turn)
                otherPlayer = Cell(int(turn)%2 + 1)
                otherTurn = Cell(int(turn)%2 + 1)
                # The minus sign assures the algorithm
                # implements a max-min solution
                bestVal = max(bestVal, -self.evaluate(table, otherPlayer, otherTurn))
                # Undo this move to properly iterate
                # through the next possible move
                table.changeCell([i,j], Cell.EMPTY)

        TableEvaluator._memo[tableHash] = bestVal
        return bestVal

    # player: the player interested on the evaluation
    # turn: who's turn it is currently
    def _hash(self, table, player, turn) -> int:
        hashVal = int(player)
        hashVal = hashVal + turn*3
        for i in range(3):
            for j in range(3):
                power = i + 3*j + 2
                coef = int(table.getCell([i,j]))
                hashVal = hashVal + coef * 3**power
        return hashVal