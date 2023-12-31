from flask import Flask, jsonify, request
import game_controller_poo
from db_games import create_tables
from exchange_rate import get_xr

app = Flask(__name__)


@app.route('/api/games', methods=["GET"])
def get_games():
    games = game_controller_poo.get_games()
    games_list=[]
    for game in games:
        elem = game.serialize()
        games_list.append(elem)
    return jsonify(games_list)

@app.route("/api/game/create", methods=["POST"])
def insert_game():
    game_details = request.get_json()
    game_code = game_details["game_code"]
    name = game_details["name"]
    num_players =game_details["num_players"]
    price = game_details["price"]
    min_age= game_details["min_age"]
    category= game_details["category"]
    platform = game_details["platform"]
    result = game_controller_poo.insert_game(game_code, name, num_players, price, min_age, category, platform)
    return jsonify(result)


@app.route("/api/game/modify", methods=["PUT"])
def update_game():
    game_details = request.get_json()
    game_code = game_details["game_code"]
    name = game_details["name"]
    num_players =game_details["num_players"]
    price = game_details["price"]
    min_age= game_details["min_age"]
    category= game_details["category"]
    platform = game_details["platform"]
    result = game_controller_poo.update_game(game_code, name, num_players, price, min_age, category, platform)
    return jsonify(result)


@app.route("/api/game/eliminate/<game_code>", methods=["DELETE"])
def delete_game(game_code):
    result = game_controller_poo.delete_game(game_code)
    return jsonify(result)


@app.route("/api/game/<game_code>", methods=["GET"])
def get_game_by_id(game_code):
    game = game_controller_poo.get_by_id(game_code)
    return jsonify(game)

@app.route("/api/game/usd/<game_code>", methods=["GET"])
def get_game_by_id_usd(game_code):
    game = game_controller_poo.get_by_id(game_code)
    xr = get_xr()
    price_usd = game['price']/xr
    game['price'] = round(price_usd,2)
    return jsonify(game)

@app.route("/api/game/<game_code>", methods=['GET'])
def get_game_by_id(game_code):
    game = game_controller_poo.get_by_id(game_code)
    if game_code == None:
        return jsonify({"error": "no date info given"})
    else:
        average_price = games.mean([int(game_code.price) for game_code in get_games])
        average_num_players = games.mean([int(game_code.num_players) for game_code in get:games])
        return jsonify({"average_price": average_price, "average_num_players": average_num_players})
create_tables()

app.run()
