import sqlite3

# Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3
#not_telegram.db
con = sqlite3.connect('not_telegram.db')
cursor = con.cursor()

# Удаляем таблицу Users, если она существует
def drop_users():
    query = '''DROP TABLE IF EXISTS users'''
    cursor.execute(query)
    con.commit()


# Создаем таблицу Users, если она не существует
def create_users():
    query = '''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER DEFAULT 10,
    balance INTEGER NOT NULL DEFAULT 1000)
    '''

    cursor.execute(query)
    con.commit()

# Заполняем таблицу 10 записями
def insert_users():
    for i in range(10):
        new_username = 'user' + str(i + 1)
        new_email = 'user' + str(i + 1) + '@user.com'
        new_age = (i + 1) * 10
        new_balance = 1000
        upd_id = i + 1

        # print(new_username,new_email, new_age, new_balance)

        params = (new_username, new_email, new_age, new_balance)

        # print(params)

        query = f'''
        INSERT INTO users (
        username,
        email,
        age,
        balance)
        VALUES (?, ?, ?, ?)
        '''

        cursor.execute(query, params)
        con.commit()


# Обновляем balance у каждой 2-ой записи начиная с 1-ой на 500:
def update_users():
    for i in range(10):
        if i % 2 != 0:
            new_balance = 500
            upd_id = i

            params = (new_balance, upd_id)

            # print(i, params)

            query = '''
            UPDATE users SET
            balance = ?
            WHERE id = ?
            '''

            cursor.execute(query, params)
            con.commit()


# Удаляем каждую 3-ю запись начиная с 1-ой
def delete_users():
    for i in range(1, 11):

        if i == 1 or i == 7:
            query = f'''
                DELETE FROM users WHERE id = {i}
                '''
            cursor.execute(query)
            con.commit()

        elif i == 4 or i == 10:
            query = f'''
                DELETE FROM users WHERE id = {i}
                '''
            cursor.execute(query)
            con.commit()


def delete_users_6():
    query = '''
    DELETE FROM users WHERE id = 6
    '''
    cursor.execute(query)
    con.commit()

def select_users_func():
    query = '''SELECT COUNT(*) AS cnt FROM Users'''
    cursor.execute(query)
    results_count = cursor.fetchone()[0]
    print(f'Общее количество записей: {results_count}')

    query = '''SELECT SUM(balance) AS sum FROM Users'''
    cursor.execute(query)
    results_sum = cursor.fetchone()[0]
    print(f'Сумма всех балансов: {results_sum}')

    query = '''SELECT AVG(balance) AS avg FROM Users'''
    cursor.execute(query)
    results_avg = cursor.fetchone()[0]
    print(f'Среднее значение баланса: {results_avg}')

drop_users()
create_users()
insert_users()
update_users()
delete_users()

# Выбор элементов и функции в SQL запросах

# Удаление из базы данных not_telegram.db записи с id = 6
delete_users_6()
select_users_func()

# Закрываем соединение
cursor.close()
con.close()




