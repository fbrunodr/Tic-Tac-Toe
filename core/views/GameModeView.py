from core.views.View import View
from core.views.GameViewTwoPlayers import GameViewTwoPlayers
from core.views.GameViewOnePlayer import GameViewOnePlayer

class GameModeView(View):

    def show(self) -> None:
        self.clearWindow()
        print("Game Mode")
        print("----------------------")
        print("1. Player vs Player")
        print("2. Player vs AI")
        print("3. Return")
        print()

    def processInput(self) -> None:
        userInput = input()

        if userInput == '1':
            gameViewTwoPlayers = GameViewTwoPlayers()
            return self.finish()
        elif userInput == '2':
            gameViewOnePlayer = GameViewOnePlayer()
            return self.finish()
        elif userInput == '3':
            return self.finish()
        else:
            print("Invalid input")
            return self.processInput()

    def finish(self) -> None:
        return