from core.model.Cell import Cell

class TableEvaluator():
    # memo is used as static variable to avoid recalculations
    _memo = {}

    # player: the player interested on the evaluation
    # turn: who's turn it is currently
    def evaluate(self, table, player, turn) -> int:
        # if it is the other player's turn, the evaluation
        # is minus the other player best move
        if player != turn:
            return -self.evaluate(table, turn, turn)

        if table.getWinner() == player:
            return 100
        if table.getWinner() == Cell.EMPTY:
            return 0
        if table.getWinner() != None:
            return -100
        
        tableHash = self._hash(table, turn)
        if tableHash in TableEvaluator._memo:
            return TableEvaluator._memo[tableHash]

        # arbitrary low value, so it changes anyway
        bestVal = -200
        for i in range(3):
            for j in range(3):
                if table.getCell([i,j]) != Cell.EMPTY:
                    continue
                table.changeCell([i,j], turn)
                otherPlayer = Cell(int(player)%2 + 1)
                # The minus sign assures the algorithm
                # implements a max-min solution
                bestVal = max(bestVal, -self.evaluate(table, otherPlayer, otherPlayer))
                # Undo this move to properly iterate
                # through the next possible move
                table.changeCell([i,j], Cell.EMPTY)

        TableEvaluator._memo[tableHash] = bestVal
        return bestVal

    # turn: who's turn it is currently
    def _hash(self, table, turn) -> int:
        hashVal = int(turn)
        for i in range(3):
            for j in range(3):
                power = 3*i + j + 1
                coef = int(table.getCell([i,j]))
                hashVal = hashVal + coef * 3**power
        return hashVal