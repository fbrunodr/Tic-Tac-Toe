from core.views.View import View
from core.views.GameModeView import GameModeView
from core.views.SettingsView import SettingsView

class MainMenuView(View):

    def show(self) -> None:
        self.clearWindow()
        print("Welcome to tic tac toe")
        print("----------------------")
        print("1. Choose Game Mode")
        print("2. Settings")
        print("3. Exit")
        print()

    def getUserInput(self) -> None:
        userInput = input()

        if userInput == '1':
            gameModeView = GameModeView()
            return self.__init__()
        elif userInput == '2':
            settingsView = SettingsView()
            return self.__init__()
        elif userInput == '3':
            return self.finish()
        else:
            print("Invalid input")
            return self.getUserInput()

    def finish(self) -> None:
        return