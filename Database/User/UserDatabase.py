import sqlite3


class User:

    def __init__(self):
        self.con = sqlite3.connect("Database/data/user.db")

        self.cur = self.con.cursor()

        self.cur.execute(f"CREATE TABLE IF NOT EXISTS user(user_id, username, name, last_name)")

    def add_user(self, user_id: int, username: str, name: str, last_name: str):
        self.cur.execute(f"""
            INSERT INTO user(user_id, username, name, last_name) VALUES
            ('{user_id}', '{username}', '{name}', '{last_name}')
        """)

        self.con.commit()

    def user_exists(self, user_id: int):
        self.cur.execute(f"""
        SELECT * FROM user WHERE user_id='{user_id}'
        """)

        self.con.commit()

        return False if self.cur.fetchone() is None else True
