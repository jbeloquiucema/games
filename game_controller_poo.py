from db_games import get_db
from clase_games import Game


def insert_game(game_code, name, num_players, price, min_age, category, platform):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO games (game_code, name, num_players, price, min_age, category, platform) \
    VALUES ( ?, ?, ?, ? ,?, ?, ?)"
    cursor.execute(statement, [game_code, name, num_players, price, min_age, category, platform])
    db.commit()
    return True

def update_game(game_code, name, num_players, price, min_age, category, platform):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE games SET name = ?, num_players = ?, min_age= ?, category= ?, platform= ? \
    WHERE game_code = ?"
    cursor.execute(statement, [name, num_players, price, min_age, category, platform, game_code])
    db.commit()
    return True


def delete_game(game_code):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM games WHERE game_code = ?"
    cursor.execute(statement, [game_code])
    db.commit()
    return True


def get_by_id(game_code):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT game_code, name, num_players, price, min_age, category, platform FROM games \
    WHERE game_code = ?"
    cursor.execute(statement, [game_code])
    single_game = cursor.fetchone()
    game_code = single_game[0]
    name = single_game[1]
    num_players = single_game[2]
    price = single_game[3]
    min_age = single_game[4]
    category = single_game[5]
    platform = single_game[6]
    game = Game (game_code, name, num_players, price, min_age, category, platform) 
    return game.serialize_details()


def get_games():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT game_code, name, num_players, price, min_age, category, platform FROM games"
    cursor.execute(query)
    game_list = cursor.fetchall()
    list_of_games=[]
    for game in game_list:
        game_code = game[0]
        name = game[1]
        num_players = game[2]
        price = game[3]
        min_age = game[4]
        category = game[5]
        platform = game[6]
        game_to_add = Game(game_code, name, num_players, price, min_age, category, platform)
        list_of_games.append(game_to_add)
    return list_of_games



