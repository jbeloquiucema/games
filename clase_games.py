class Game:

    def __init__(self, game_code, name,num_players, price, min_age, category, platform) -> None:
        self.game_code = game_code
        self.name = name
        self.num_players = num_players
        self.price = price
        self.min_age = min_age
        self.category = category
        self.platform = platform


    def serialize(self):
        return {
            'game_code': self.game_code,
            'name': self.name,
            'platform': self.platform,
            'price': self.price
        }

    def serialize_details(self):
        return {
            'game_code': self.game_code,
            'name': self.name,
            'num_players': self.num_players,
            'price': self.price,
            'min_age': self.min_age,
            'category': self.category,
            'platform': self.platform
        }
