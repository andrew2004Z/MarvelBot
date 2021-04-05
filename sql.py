import sqlite3


class sqll_user:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(
            database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def user_in_base(self, user_id):
        with self.connection:
            result = self.cursor.execute(
                'SELECT * FROM `users_info` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def get_col_proj(self, user_id):
        get_q = f'SELECT col_proj FROM users_info WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            return int(str(result[0])[1:-2])

    def update_col_proj(self, user_id, col_quetions):
        """Обновляем количество прочтений"""
        with self.connection:
            return self.cursor.execute("UPDATE `users_info` SET `col_proj` = ? WHERE `user_id` = ?", (col_quetions, user_id))

    def add_user(self, user_id, reg_date, col_proj):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users_info' ('user_id', 'reg_date', 'col_proj') VALUES (?,?,?)", (user_id, reg_date, col_proj))


class sqll_comics:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
    
    def get_id_pdf(self, comics_name):
        get_q = f'SELECT comics_id FROM comics WHERE comics_name = "{comics_name}";'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            return str(result[0])[1:-2]

    def get_cover_id(self, comics_name):
        get_q = f'SELECT cover_id FROM comics WHERE comics_name = "{comics_name}";'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            return str(result[0])[1:-2]

    def get_coll_page(self, comics_name):
        get_q = f'SELECT coll_page FROM comics WHERE comics_name = "{comics_name}";'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            return int(str(result[0])[1:-2])

    def comics_in_base(self, name):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `comics` WHERE `comics_name` = ?', (name,)).fetchall()
            return bool(len(result))

    def add_comics(self, name, comics_id, cover_id, coll_page):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'comics' ('comics_name', 'comics_id', 'cover_id', 'coll_page') VALUES (?,?,?,?)", (name, comics_id, cover_id, coll_page))