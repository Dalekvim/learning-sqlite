import sqlite3

# Data types include:
# Null
# Integer
# Real
# Text
# Blob

with sqlite3.connect('sqlite.db') as conn:
    cursor = conn.cursor()
    # cursor.execute(
    #     """CREATE TABLE customers (
    #         first_name text,
    #         last_name text,
    #         email text
    #     )"""
    # )
    # cursor.execute(
    #     """INSERT INTO customers
    #     VALUES (
    #         'John',
    #         'Elder',
    #         'john@codemy.com'
    #     )"""
    # )
    cursor.execute("""SELECT * FROM customers""")
    print(cursor.fetchall())

    conn.commit()
