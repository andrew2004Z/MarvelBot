import sqlite3

class sqll:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
    
    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `user_info` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def get_col_proj(self, user_id):
        get_q = f'SELECT col_proj FROM user_info WHERE user_id = {user_id};'
        with self.connection:
            result = self.cursor.execute(get_q).fetchall()
            return int(str(result[0])[1:-2])

    def update_col_proj(self, user_id, col_quetions):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `user_info` SET `col_proj` = ? WHERE `user_id` = ?", (col_quetions, user_id))

    def update_col_erorr(self, user_id, col_erorr):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `user_info` SET `col_erorr` = ? WHERE `user_id` = ?", (col_erorr, user_id))

    def add_user(self, user_id, col_quetions=0, col_erorr=0):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'user_info' ('user_id', 'col_quetions', 'col_erorr') VALUES (?,?,?)", (user_id, col_quetions, col_erorr))