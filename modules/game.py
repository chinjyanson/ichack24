from modules import AssetManager
class top:
    def __init__(self) -> None:
        self.games = []
        pass

    def new_game(self) -> None:
        self.games.append(Game())
        return self.games[-1]

class Game:
    def __init__(self) -> None:
        self.players = {}
        pass

    def new_player(self,id) -> None:
        self.games[id] = Game()


class Player:
    def __init__(self) -> None:
        self.assetManager = AssetManager.AssetManager()
        pass