from abc import ABC, abstractmethod
import os
import platform

class View(ABC):
    def __init__(self) -> None:
        self.show()
        self.getUserInput()

    @abstractmethod
    def show(self) -> None:
        pass

    @abstractmethod
    def getUserInput(self) -> None:
        pass

    @abstractmethod
    def finish(self) -> None:
        pass

    def clearWindow(self):
        if platform.system()=="Windows":
            os.system('cls')
        else:
            os.system('clear')