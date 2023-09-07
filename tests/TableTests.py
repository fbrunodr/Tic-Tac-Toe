from core.model.Table import table
from core.model.Cell import Cell

table.clear()

table.changeCell(1,1, Cell.CROSS)

assert table.getCell(1,1) == Cell.CROSS
assert table.getCell(0,0) == Cell.EMPTY
assert table.getCell(2,1) == Cell.EMPTY
assert table.getWinner() == None

table.changeCell(2,0, Cell.CROSS)

assert table.getCell(2,0) == Cell.CROSS
assert table.getCell(0,2) == Cell.EMPTY
assert table.getWinner() == None

table.changeCell(0,2, Cell.CIRCLE)

assert table.getCell(0,2) == Cell.CIRCLE
assert table.getWinner() == None

table.changeCell(1,2, Cell.CIRCLE)

assert table.getCell(1,2) == Cell.CIRCLE
assert table.getWinner() == None

table.changeCell(2,2, Cell.CIRCLE)

assert table.getWinner() == Cell.CIRCLE

table.changeCell(2,2, Cell.CROSS)

assert table.getCell(2,2) == Cell.CROSS
assert table.getWinner() == None

table.changeCell(0,0, Cell.CROSS)

assert table.getCell(0,0) == Cell.CROSS
assert table.getWinner() == Cell.CROSS

table.changeCell(0,0, Cell.EMPTY)

assert table.getWinner() == None

table.changeCell(2,1, Cell.CROSS)

assert table.getWinner() == Cell.CROSS

print("All table tests passed")