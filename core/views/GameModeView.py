from core.views.View import View
from core.views.GameViewTerminalTwoPlayers import GameViewTerminalTwoPlayers
from core.views.GameViewTerminalOnePlayer import GameViewTerminalOnePlayer

class GameModeView(View):

    def show(self) -> None:
        self.clearWindow()
        print("Game Mode")
        print("----------------------")
        print("1. Player vs Player")
        print("2. Player vs AI")
        print("3. Return")
        print()

    def getUserInput(self) -> None:
        userInput = input()

        if userInput == '1':
            gameViewTerminalTwoPlayers = GameViewTerminalTwoPlayers()
            return self.finish()
        elif userInput == '2':
            gameViewTerminalOnePlayer = GameViewTerminalOnePlayer()
            return self.finish()
        elif userInput == '3':
            return self.finish()
        else:
            print("Invalid input")
            return self.getUserInput()

    def finish(self) -> None:
        return