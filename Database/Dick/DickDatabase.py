import datetime
import random
import sqlite3


class Dick:

    def __init__(self):
        self.con = sqlite3.connect("Database/data/dick.db")

        self.cur = self.con.cursor()

        self.cur.execute(f"CREATE TABLE IF NOT EXISTS dick(user_id, size, last_update)")

    def create_dick(self, user_id: int):
        self.cur.execute(f"""
            INSERT INTO dick(user_id, size, last_update) VALUES
            ({user_id}, {random.randint(-10, 10)}, '{datetime.datetime.now()}')
        """)

        self.con.commit()

    def update_dick(self, user_id: int):
        if not self.last_update(user_id):
            return None

        number = random.randint(-10, 10)

        self.cur.execute(f"""
        UPDATE dick SET size=size+{number} WHERE user_id={user_id}
        """)

        self.con.commit()

        return number

    def last_update(self, user_id: int):
        self.cur.execute(f"""
        SELECT last_update FROM dick WHERE user_id={user_id}
        """)

        self.con.commit()

        time = self.cur.fetchone()

        if time is None:
            return False

        if (datetime.datetime.now() - datetime.datetime.strptime(time[0], "%Y-%m-%d %H:%M:%S.%f")).seconds // 3600 > 12:
            return True

        return False
