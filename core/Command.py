from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self) -> None:
        self._isExecuted = False
        self._isReduable = False

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

    @abstractmethod
    def redo(self) -> None:
        pass

    def isExecuted(self) -> bool:
        return self._isExecuted

    def isReduable(self) -> bool:
        return self._isReduable