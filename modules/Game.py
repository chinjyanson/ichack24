from modules.AssetManager import AssetManager

class top:
    def __init__(self) -> None:
        self.games = []
        pass

    def new_game(self) -> None:
        self.games[len(self.games)] = Game()

class Game:
    def __init__(self) -> None:
        self.players = {}

        self.assetManager = AssetManager()
        
    
        pass

    def new_player(self,session) -> None:
        self.games[session] = Game()


class Player:
    def __init__(self) -> None:
        pass