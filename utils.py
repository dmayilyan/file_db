import sqlite3


def load_sql_script(path_to_file: str):
    with open(path_to_file, "r") as sql_file:
        sql_script = sql_file.read()

    return sql_script


def get_cursor(db_name):
    with sqlite3.connect(db_name, isolation_level=None) as con:
        print("WARNING: Isolattion level is set to 'None'")
        cur = con.cursor()

    return cur
