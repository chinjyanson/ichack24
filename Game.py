import random
game_id_count = 0
player_id_count = 0
used_game_codes = {}

def new_game_code():
    code = random.randint(0,9999)
    while used_game_codes[code] == true:
        code = random.randint(0,9999)
    used_game_codes += code;
    return code

class Game:

    def __init__(self) -> None:
        self.players = []
        self.uid = game_id_count
        id_count += 1
        self.join_code = new_game_code()
        self.players = []
    
    def get_join_code(self) -> str:
        return '{self.}'.format('5'.zfill(2))
    
    def set_session(self, cookie):
        self.session = cookie
        return cookie

class Player:

    def __init__(self) -> None:
        self.name
        self.id = player_id_count
        player_id_count += 1