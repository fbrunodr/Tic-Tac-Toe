from core.GameManager import gameManager
from core.commands.ChangeCellCommand import ChangeCellCommand
from core.model.Cell import Cell
from core.model.Table import table

table.clear()
gameManager.clear()

gameManager.executeCommand(ChangeCellCommand([1,2], Cell.CROSS))

assert table.getCell([1,2]) == Cell.CROSS
assert table.getCell([0,0]) == Cell.EMPTY
assert table.getCell([2,1]) == Cell.EMPTY
assert table.getWinner() == Cell.EMPTY

gameManager.executeCommand(ChangeCellCommand([1,2], Cell.CIRCLE))

assert table.getCell([1,2]) == Cell.CIRCLE
assert table.getCell([1,0]) == Cell.EMPTY
assert table.getWinner() == Cell.EMPTY

gameManager.undo()

assert table.getCell([1,2]) == Cell.CROSS
assert table.getWinner() == Cell.EMPTY

gameManager.undo()

assert table.getCell([1,2]) == Cell.EMPTY

gameManager.redo()

assert table.getCell([1,2]) == Cell.CROSS

gameManager.executeCommand(ChangeCellCommand([1,1], Cell.CIRCLE))

assert table.getCell([1,1]) == Cell.CIRCLE

gameManager.redo()

assert table.getCell([1,1]) == Cell.CIRCLE

gameManager.executeCommand(ChangeCellCommand([2,0], Cell.CIRCLE))
gameManager.executeCommand(ChangeCellCommand([0,2], Cell.CIRCLE))

assert table.getWinner() == Cell.CIRCLE

gameManager.undo()
gameManager.undo()
gameManager.undo()
gameManager.executeCommand(ChangeCellCommand([1,0], Cell.CIRCLE))
gameManager.redo()
gameManager.redo()
gameManager.redo()

assert table.getWinner() == Cell.EMPTY
assert table.getCell([1,2]) == Cell.CROSS
assert table.getCell([1,0]) == Cell.CIRCLE
assert table.getCell([1,1]) == Cell.EMPTY