from flask import Flask, jsonify, request
import game_controller_poo
from db_games import create_tables
from exchange_rate import get_xr

app = Flask(__name__)


@app.route('/games', methods=["GET"])
def get_games():
    games = game_controller_poo.get_games()
    games_list=[]
    for game in games:
        elem = game.serialize()
        games_list.append(elem)
    return jsonify(games_list)

@app.route("/game/create", methods=["POST"])
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


@app.route("/game/modify", methods=["PUT"])
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


@app.route("/game/eliminate/<game_code>", methods=["DELETE"])
def delete_game(game_code):
    result = game_controller_poo.delete_game(game_code)
    return jsonify(result)


@app.route("/game/<game_code>", methods=["GET"])
def get_game_by_id(game_code):
    game = game_controller_poo.get_by_id(game_code)
    return jsonify(game)

@app.route("/game/usd/<game_code>", methods=["GET"])
def get_game_by_id_usd(game_code):
    game = game_controller_poo.get_by_id(game_code)
    xr = get_xr()
    price_usd = game['price']/xr
    game['price'] = round(price_usd,2)
    return jsonify(game)

create_tables()

app.run()
