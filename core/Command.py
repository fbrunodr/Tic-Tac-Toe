from abc import ABC, abstractmethod

class Command(ABC):
    _isExecuted = False
    _isReduable = False

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