import sqlite3
DATABASE_NAME = "games.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS games(
                game_code INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                num_players INTEGER NOT NULL,
                price REAL NOT NULL,
                min_age INTEGER NOT NULL,
                category TEXT NOT NULL,
                platform INTEGER NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
