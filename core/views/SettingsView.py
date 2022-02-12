from core.Observer import Observer
from core.views.View import View
from core.Settings import settings
from core.model.Cell import Cell

class SettingsView(View, Observer):
    def __init__(self) -> None:
        settings.addObserver(self)
        super().__init__()

    def update(self) -> None:
        return self.show()

    def show(self) -> None:
        self.clearWindow()
        print("Setting")
        print("----------------------")

        line1 = "1. [?] Start With Circle"
        if settings.getFirstToPlay() == Cell.CIRCLE:
            line1 = line1.replace('?', 'X')
        else:
            line1 = line1.replace('?', ' ')
        print(line1)

        line2 = "2. [?] AI plays first"
        if settings.AIplayFirst():
            line2 = line2.replace('?', 'X')
        else:
            line2 = line2.replace('?', ' ')
        print(line2)

        print("3. Back")
        print()

    def processInput(self) -> None:
        userInput = input("Choose a option to change it: ")

        if userInput == '1':
            val = settings.getFirstToPlay()
            val = Cell(int(val)%2 + 1)
            settings.setFirstToPlay(val)
            return self.processInput()
        elif userInput == '2':
            settings.setAIstarts(not settings.AIplayFirst())
            return self.processInput()
        elif userInput == '3':
            return self.finish()
        else:
            print("Invalid input")
            return self.processInput()

    def finish(self) -> None:
        settings.deleteObserver(self)
        return