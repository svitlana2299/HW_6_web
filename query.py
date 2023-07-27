import sqlite3


def execute_query(file_name):
    # Підключення до бази даних SQLite3
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()

    # Виконання SQL-запиту з файлу
    with open(file_name, "r") as file:
        sql_query = file.read()
        cursor.execute(sql_query)

    # Отримання результатів
    results = cursor.fetchall()

    # Виведення результатів списком кортежів
    for row in results:
        print(row)

    # Закриття з'єднання
    cursor.close()
    connection.close()


# Виконати запит query_1.sql
print("Query 1 results:")
execute_query("query_1.sql")

# Виконати запит query_2.sql
print("Query 2 results:")
execute_query("query_2.sql")

# Виконати запит query_3.sql
print("Query 3 results:")
execute_query("query_3.sql")

# Виконати запит query_4.sql
print("Query 4 results:")
execute_query("query_4.sql")

# Виконати запит query_5.sql
print("Query 5 results:")
execute_query("query_5.sql")

# Виконати запит query_6.sql
print("Query 6 results:")
execute_query("query_6.sql")

# Виконати запит query_7.sql
print("Query 7 results:")
execute_query("query_7.sql")

# Виконати запит query_8.sql
print("Query 8 results:")
execute_query("query_8.sql")

# Виконати запит query_9.sql
print("Query 9 results:")
execute_query("query_9.sql")

# Виконати запит query_10.sql
print("Query 10 results:")
execute_query("query_10.sql")

# Виконати запит query_11.sql
print("Query 11 results:")
execute_query("query_11.sql")

# Виконати запит query_12.sql
print("Query 12 results:")
execute_query("query_12.sql")
