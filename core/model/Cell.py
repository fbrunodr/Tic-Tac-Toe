from enum import IntEnum

class Cell(IntEnum):
    EMPTY = 0
    CROSS = 1
    CIRCLE = 2

    def __str__(self) -> str:
        if self == Cell.EMPTY:
            return ' '
        elif self == Cell.CROSS:
            return 'X'
        elif self == Cell.CIRCLE:
            return 'O'
        else:
            raise("Cell type unkown. Can't parse to str.")