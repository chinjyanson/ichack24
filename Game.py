import random
id_count = 0
used_game_codes = {}

def new_game_code():
    code = random.randint(0,9999)
    


class Game:

    def __init__(self) -> None:
        self.players = []
        self.uid = id_count
        id_count += 1
        join_code = new_game_code()

class Player: